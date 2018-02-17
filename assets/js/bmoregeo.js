/**
 * Created by christopherfricke on 3/14/15.
 */

var availableMaps = ['bmoregeo.map-4rkgt9ta'];
var center = [39.2933, -76.6167];
var zoom = 15;


var selectedMap = availableMaps[Math.floor(Math.random()*availableMaps.length)];
var map = L.mapbox.map('map', selectedMap, {zoomControl: false})
    .setView(center, zoom);