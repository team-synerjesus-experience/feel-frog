'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', [
  'ngRoute',
  'myApp.filters',
  'myApp.services',
  'myApp.directives',
  'myApp.controllers'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/input', {templateUrl: 'partials/input.html', controller: 'MyCtrl1'});
  $routeProvider.when('/output', {templateUrl: 'partials/output.html', controller: 'MyCtrl1'});
  $routeProvider.otherwise({redirectTo: '/input'});
}]);
