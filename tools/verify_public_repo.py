#!/usr/bin/env python3
from __future__ import annotations
import csv, hashlib, json, re, sys, zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

REQUIRED = [
    'README.md','LICENSE','CHANGELOG.md','SHA256SUMS','SECURITY.md','CONTRIBUTING.md','CODE_OF_CONDUCT.md',
    '.github/FUNDING.yml','.github/workflows/verify.yml','.github/workflows/pages.yml',
    'docs/index.html','docs/styles.css','docs/app.js','docs/404.html','docs/robots.txt','docs/.nojekyll','docs/assets/icon.svg','docs/assets/social-card.png',
    'docs/INSTALL-CODEX.md','docs/INSTALL-CLAUDE.md','docs/INSTALL-AGENT-SKILL.md','docs/SAFETY.md','docs/FAQ.md','docs/FUNDING.md','docs/PARTNERS.md','docs/BENCHMARKS.md',
    'distributions/codex/bitcoin-mining-troubleshooter-codex-v1.1.0.zip',
    'distributions/claude/bitcoin-mining-troubleshooter-claude-v1.1.0.zip',
    'distributions/agent-skill/bitcoin-mining-troubleshooter-agent-skill-v1.1.0.zip',
    'demos/01-fleet-restart-recovery.csv','demos/02-network-segment-incident.xlsx','demos/03-power-thermal-operations.xlsx','demos/04-repair-history.jsonl','demos/05-miner-log-corpus.ndjson','demos/README.md','demos/DEMO-SCRIPT.md',
]
FORBIDDEN_PATH_FRAGMENTS=('evaluator','answer-key','expected-findings','scoring-rubric','source-v1.1.0','private-build-notes','recovery-bundle','superpowers/specs','superpowers/plans')
# sha256 of exact private-only implementation phrases; hashes keep those names out of the public checker itself.
FORBIDDEN_PHRASE_HASHES={
'894a8d93b9f89185e33284593c43cccb0c4d6680d5d1fe951fd2673d1912c983',
'815f94d3988f1a263b92da6a879dd251d0bbb291b01fa64d94ff2d7a08f384e6',
'41c84736b322c96e9c4e2dbfd7580b138d275d5108ba0e8a47ad1f707c37068e',
}
TEXT_SUFFIXES={'.md','.txt','.json','.jsonl','.ndjson','.yaml','.yml','.html','.css','.js','.csv','.svg','.py'}
TOKEN_RE=re.compile(r'[a-z0-9]+')
REPO='KurtusCobain/ASIC-Intelligence-Plugin-Skill-Package'

def _digest(s:str)->str:return hashlib.sha256(s.encode()).hexdigest()
def _read(path:Path):
    if path.suffix.lower() not in TEXT_SUFFIXES:return None
    try:return path.read_text(encoding='utf-8',errors='ignore')
    except OSError:return None

def _phrase_hits(text:str):
    tokens=TOKEN_RE.findall(text.lower()); hits=[]
    for n in (1,2,3):
        for i in range(max(0,len(tokens)-n+1)):
            phrase=' '.join(tokens[i:i+n])
            if _digest(phrase) in FORBIDDEN_PHRASE_HASHES:
                hits.append(_digest(phrase)[:12])
    return sorted(set(hits))

def _zip_errors(path:Path):
    errs=[]
    try:
        with zipfile.ZipFile(path) as zf:
            bad=zf.testzip()
            if bad: errs.append(f'bad-zip-member:{path.name}:{bad}')
            for m in zf.infolist():
                low=m.filename.lower()
                if any(x in low for x in FORBIDDEN_PATH_FRAGMENTS):errs.append(f'forbidden-zip-path:{path.name}:{m.filename}')
    except zipfile.BadZipFile:errs.append(f'invalid-zip:{path.name}')
    return errs

def _xlsx_data_rows(path:Path, sheet_name:str)->int:
    main_ns = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
    rel_ns = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    pkg_rel_ns = 'http://schemas.openxmlformats.org/package/2006/relationships'
    with zipfile.ZipFile(path) as zf:
        workbook = ET.fromstring(zf.read('xl/workbook.xml'))
        rels = ET.fromstring(zf.read('xl/_rels/workbook.xml.rels'))
        targets = {r.attrib['Id']: r.attrib['Target'] for r in rels.findall(f'{{{pkg_rel_ns}}}Relationship')}
        target = None
        for sheet in workbook.findall(f'.//{{{main_ns}}}sheet'):
            if sheet.attrib.get('name') == sheet_name:
                target = targets[sheet.attrib[f'{{{rel_ns}}}id']]
                break
        if target is None:
            raise ValueError(f'missing worksheet {sheet_name!r} in {path.name}')
        member = target.lstrip('/')
        if not member.startswith('xl/'):
            member = 'xl/' + member
        root = ET.fromstring(zf.read(member))
        rows = root.findall(f'.//{{{main_ns}}}row')
        return max(0, len(rows) - 1)

def demo_counts(root:Path)->dict[str,int]:
    demos = root/'demos'
    with (demos/'01-fleet-restart-recovery.csv').open(encoding='utf-8') as fh:
        fleet=max(0,sum(1 for _ in fh)-1)
    network=_xlsx_data_rows(demos/'02-network-segment-incident.xlsx','Fleet')
    thermal=_xlsx_data_rows(demos/'03-power-thermal-operations.xlsx','MinerSnapshot')
    repair_ids=set()
    with (demos/'04-repair-history.jsonl').open(encoding='utf-8') as fh:
        for line in fh:
            if line.strip():
                miner_id=json.loads(line).get('miner_id')
                if miner_id: repair_ids.add(str(miner_id))
    with (demos/'05-miner-log-corpus.ndjson').open(encoding='utf-8') as fh:
        logs=sum(1 for line in fh if line.strip())
    return {
        'fleet_restart': fleet,
        'network_incident': network,
        'power_thermal': thermal,
        'repair_miners': len(repair_ids),
        'miner_logs': logs,
    }

def _demo_count(root:Path)->int:
    return sum(demo_counts(root).values())

def verify_repo(root:Path):
    errors=[]
    for rel in REQUIRED:
        if not (root/rel).is_file():errors.append(f'missing:{rel}')
    for p in root.rglob('*'):
        if '.git' in p.parts or not p.is_file():continue
        rel=str(p.relative_to(root)).lower()
        if any(x in rel for x in FORBIDDEN_PATH_FRAGMENTS):errors.append(f'forbidden-path:{rel}')
        if p.suffix.lower()=='.zip':errors.extend(_zip_errors(p));continue
        text=_read(p)
        if text:
            for hit in _phrase_hits(text):errors.append(f'forbidden-private-phrase:{p.relative_to(root)}:{hit}')
            old_repo='KurtusCobain/'+'bitcoin-mining-troubleshooter'
            if old_repo in text:errors.append(f'outdated-repo-url:{p.relative_to(root)}')
    if (root/'README.md').is_file():
        readme=(root/'README.md').read_text(encoding='utf-8')
        for s in ('ASIC Intelligence Plugin/Skill Package','Bitcoin Mining Troubleshooter','Powered by ASIC Intelligence','Use it. Integrate it. Fund it.'):
            if s not in readme:errors.append(f'readme-missing:{s}')
        if '20,000' in readme and _demo_count(root)<20000:errors.append('demo-count-below-public-claim')
    if (root/'docs/index.html').is_file():
        html=(root/'docs/index.html').read_text(encoding='utf-8')
        for s in ('Try a fleet-scale demo','Install for Codex','Install for Claude','Founding Design Partner','Use it. Integrate it. Fund it.'):
            if s not in html:errors.append(f'site-missing:{s}')
        if 'href="../demos/' in html or 'href="../distributions/' in html:errors.append('site-pages-relative-download-link')
        for s in ('21,470','Illustrative diagnostic example','NOT PART OF v1.1.0','mailto:austin@wnclogiclab.com','og:title','og:description','og:image','canonical'):
            if s not in html:errors.append(f'site-release-missing:{s}')
    if (root/'.github/FUNDING.yml').is_file() and 'KurtusCobain' not in (root/'.github/FUNDING.yml').read_text():errors.append('funding-maintainer-missing')
    pages=root/'.github/workflows/pages.yml'
    if pages.is_file():
        y=pages.read_text()
        for s in ('actions/configure-pages@v5','actions/upload-pages-artifact@v4','actions/deploy-pages@v4','path: docs','pages: write','id-token: write'):
            if s not in y:errors.append(f'pages-workflow-missing:{s}')
    return sorted(set(errors))

def main():
    root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve();errors=verify_repo(root)
    if errors:
        print('PUBLIC REPO: FAIL');[print('-',e) for e in errors];return 1
    print('PUBLIC REPO: PASS')
    print('- required public files and v1.1.0 artifacts present')
    print('- distribution ZIP integrity checks pass')
    print('- public/private path and phrase guards clean')
    print(f'- synthetic primary-record scale: {_demo_count(root):,}')
    print('- GitHub Pages and funding configuration present')
    return 0
if __name__=='__main__':raise SystemExit(main())
