
var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/css/estilos.css',
    '/static/img/logofloreria.png',
    'galeria/',
    '/ingresar',
    '/carrito',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {

          return fetch(event.request)
          .catch(function(rsp) {
             return response; 
          });
          
          
        })
    );
});


//solo para cachear todo reemplazar por esta versión del Fetch


self.addEventListener('fetch', function(event) {
    event.respondWith(

      fetch(event.request)
      .then((result)=>{
        return caches.open(CACHE_NAME)
        .then(function(c) {
          c.put(event.request.url, result.clone())
          return result;
        })
        
      })
      .catch(function(e){
          return caches.match(event.request)
      })
    );
});

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
  apiKey: "AIzaSyBkv9rff7oJk5O0mSVV3Bu4GO0ppObR5_c",
  authDomain: "floreria-6289c.firebaseapp.com",
  databaseURL: "https://floreria-6289c.firebaseio.com",
  projectId: "floreria-6289c",
  storageBucket: "floreria-6289c.appspot.com",
  messagingSenderId: "325885603760",
  appId: "1:325885603760:web:51912bbde164fd917ab075"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload){

  let title = 'titulo de la notifiacion';

        let options = {
          body:'Este Mensaje',
          icon:'/static/img/logofloreria.png'
        }

        self.ServiceWorkerRegistration.showNotification(title,options);

});
