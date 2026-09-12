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
if (button && nav) {
  button.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    button.setAttribute('aria-expanded', String(open));
  });
  nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
    nav.classList.remove('open');
    button.setAttribute('aria-expanded', 'false');
  }));
}
