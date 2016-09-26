'use strict';

angular.module('eventapp', [
  'ui.router',
  'ngResource',
  'eventapp.events.controllers',
  'eventapp.events.services'
]);

angular.module('eventapp').config(config);

config.$inject = [
  '$interpolateProvider',
  '$httpProvider',
  '$resourceProvider',
  '$stateProvider',
  '$urlRouterProvider'
];

function config(
  $interpolateProvider,
  $httpProvider,
  $resourceProvider,
  $stateProvider,
  $urlRouterProvider){
    // Force angular to use square brackets for template tag
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // It makes dealing with Django slashes at the end of everything easier.
    $resourceProvider.defaults.stripTrailingSlashes = false;

    // Routing
    $urlRouterProvider.otherwise('/events');
    $stateProvider
      .state('events', {
        url: '/events',
        templateUrl: 'static/partials/events/events.html',
        controller: 'EventsController'
      })
      .state('eventDetail', {
        url: '/events/:id',
        templateUrl: 'static/partials/events/register.html',
        controller: 'EventDetailController'
      })
  }
