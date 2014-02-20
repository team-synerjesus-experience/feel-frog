'use strict';

/* Directives */


angular.module('myApp.directives', []).

directive('setMoodColor', function($scope) {
 
      function link(scope, element, attrs) {
        element.style.backgroundColor="blue";
        function updateTime() {
        element.style.backgroundColor="blue";
        };
    }
});
