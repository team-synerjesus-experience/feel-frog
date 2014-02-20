'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
  controller('MyCtrl1', ['$scope', '$log', function($s, $log) {

  		//mock data
  		 $s.data={

	  		interval_1h:[
	  			{
	  				time:'14/02/25 15:00-16:00',
	  				activities: ['School', 'Social'],
	  				mood:'5',
	  			},

	  			{
	  				time:'14/02/25 17:00-18:00',
	  				activities: ['School', 'Social', 'loling'],
	  				mood:'2',
	  			},

	  			{
	  				time:'14/02/25 18:00-19:00',
	  				activities: ['School', 'Social', 'rofling'],
	  				mood:'1',
	  			}
	  		],

	  		interval_6h:[
	  			{
	  				activities: ['School', 'Social', 'something else'],
	  				mood:'2',
	  				time:'14/02/25 12:00-18:00'
	  			},

	  			{
	  				activities: ['School', 'work', 'something else'],
	  				mood:'3',
	  				time:'14/02/25 12:00-18:00'
	  			},
	  	]
	  };
  	//init

  		$s.currentIntervals=$s.data.interval_1h
			$log.log($s.displayInterval);
			$s.displayInterval=$s.data.interval_1h[0]
		//


  		$s.chooseInterval = function(interval){
  			$s.displayInterval=interval;
  		};
  		
  		$log.log($s.displayInterval.mood);



  		$s.getColor = function(interval){
  			if(interval.mood==5){
  			return "{backgroundColor:'blue'}";
  			}
  			else return "{backgroundColor:'red'}";
  		};


	  	if($s.displayInterval.mood==2){
	  		$log.log($s.displayInterval.mood);
	  	  $s.moodColor = "{backgroundColor:'blue'}";
	  	}

	}




]);