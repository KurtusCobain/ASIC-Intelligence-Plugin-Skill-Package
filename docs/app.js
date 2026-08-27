const GA4_MEASUREMENT_ID = 'G-EGDNX281X0';
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', GA4_MEASUREMENT_ID);

const googleTag = document.createElement('script');
googleTag.async = true;
googleTag.src = 'https://www.googletagmanager.com/gtag/js?id=G-EGDNX281X0';
document.head.appendChild(googleTag);

const button=document.querySelector('.menu-button');const nav=document.querySelector('#site-nav');if(button&&nav){button.addEventListener('click',()=>{const open=nav.classList.toggle('open');button.setAttribute('aria-expanded',String(open));});nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');button.setAttribute('aria-expanded','false');}));}
