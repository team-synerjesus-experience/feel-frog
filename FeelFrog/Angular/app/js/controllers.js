'use strict';

/* Controllers */

angular.module('myApp.controllers', ['$scope', '$route', '$routeParams', '$location']).
  controller('MyCtrl', [function($scope, $route, $routeParams, $location) {
    $scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;
  }]);
