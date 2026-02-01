// Basic Service Worker for PWA installation
self.addEventListener('install', (event) => {
  console.log('Service Worker: Installed');
});

self.addEventListener('fetch', (event) => {
  // We can add caching logic here later
  event.respondWith(fetch(event.request));
});
