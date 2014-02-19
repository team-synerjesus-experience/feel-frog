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
  $routeProvider.when('/index,' {templateUrl: 'partials/input.html', controller: 'MyCtrl'});
  $routeProvider.when('/output', {templateUrl: 'partials/output.html', controller: 'MyCtrl'});
  $routeProvider.otherwise({redirectTo: 'localhost:8000/app/partials/view1'});
}]);
