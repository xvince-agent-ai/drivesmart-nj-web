import { injectSpeedInsights } from '@vercel/speed-insights';

injectSpeedInsights({ framework: 'vite' });

const toggle = document.querySelector('.nav-toggle');
const links = document.querySelector('#nav-links');

toggle?.addEventListener('click', () => {
  const open = links.classList.toggle('open');
  toggle.setAttribute('aria-expanded', String(open));
});

links?.querySelectorAll('a').forEach((anchor) => {
  anchor.addEventListener('click', () => {
    links.classList.remove('open');
    toggle?.setAttribute('aria-expanded', 'false');
  });
});
