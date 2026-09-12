const GA4_MEASUREMENT_ID = 'G-EGDNX281X0';
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', GA4_MEASUREMENT_ID);

const googleTag = document.createElement('script');
googleTag.async = true;
googleTag.src = 'https://www.googletagmanager.com/gtag/js?id=G-EGDNX281X0';
document.head.appendChild(googleTag);

const conversionEvents = new Set([
  'chatgpt_plugin_click',
  'youtube_demo_click',
  'package_download',
  'demo_file_open',
  'demo_prompt_copy',
  'github_repo_click',
  'desktop_interest_click',
  'partner_contact_click',
  'founder_profile_click',
]);

function trackConversion(element) {
  const eventName = element.dataset.track;
  if (!conversionEvents.has(eventName)) return;

  const params = {
    placement: element.dataset.placement || undefined,
    package_type: element.dataset.package || undefined,
    version: element.dataset.version || undefined,
    demo: element.dataset.demo || undefined,
    destination: element.href || undefined,
    page: window.location.pathname,
  };

  try {
    if (typeof window.gtag === 'function') {
      window.gtag('event', eventName, params);
    } else if (typeof gtag === 'function') {
      gtag('event', eventName, params);
    }
  } catch (_) {
    // Analytics must never block navigation or break the static site.
  }
}

document.querySelectorAll('[data-track]').forEach((element) => {
  element.addEventListener('click', () => trackConversion(element));
});

const button = document.querySelector('.menu-button');
const nav = document.querySelector('#site-nav');

function closeMenu() {
  if (!button || !nav) return;
  nav.classList.remove('open');
  button.setAttribute('aria-expanded', 'false');
}

if (button && nav) {
  button.addEventListener('click', (event) => {
    event.stopPropagation();
    const open = nav.classList.toggle('open');
    button.setAttribute('aria-expanded', String(open));
  });

  nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      closeMenu();
      button.focus();
    }
  });

  document.addEventListener('click', (event) => {
    if (!nav.classList.contains('open')) return;
    if (!nav.contains(event.target) && !button.contains(event.target)) closeMenu();
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 980) closeMenu();
  });
}

document.querySelectorAll('.copy-prompt').forEach((control) => {
  control.addEventListener('click', async () => {
    const prompt = control.dataset.prompt;
    if (!prompt) return;

    try {
      await navigator.clipboard.writeText(prompt);
      const originalText = control.textContent;
      control.textContent = 'Copied';
      control.classList.add('copied');
      window.setTimeout(() => {
        control.textContent = originalText;
        control.classList.remove('copied');
      }, 1800);
    } catch (_) {
      // Clipboard support can be blocked by the browser; leave the visible prompt available.
    }
  });
});
