'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
  controller('MyCtrl1', ['$scope', '$log', '$http',function($s, $log) {

  		//mock data

  /*		$http.get('/someUrl').success(successCallback);{
  			$s.data=successCallback;
  		}
*/
  		 $s.data={


	  		interval_6h:[
	  			{
	  				time:'14/02/25 12:00-18:00',
	  				mood:'5',
	  				activities: [
	  					{description:'studying in the university', //list should be ordered by time
	  					timetag: '12.00-13.00'},

	  					{description:'studying in the university',
	  					timetag: '14.00-15.00'},

	  					{description:'studying in the university',
	  					timetag: '16.00-17.00'},
	  				]
	  			},

	  			{
	  				time:'14/02/25 12:00-18:00',
	  				mood:'2',
	  				activities: [
	  					{description:'studying in the university', //list should be ordered by time
	  					timetag: '12.00-13.00'},

	  					{description:'studying in the university',
	  					timetag: '14.00-15.00'},

	  					{description:'studying in the university',
	  					timetag: '16.00-17.00'},
	  				]
	  			}

	  		],

	  		interval_12h:[
	  			{
	  				time:'14/02/25 12:00-18:00',
	  				mood:'1',
	  				activities: [
	  					{description:'studying in the university', //list should be ordered by time
	  					timetag: '12.00-13.00'},

	  					{description:'studying in the university',
	  					timetag: '14.00-15.00'},

	  					{description:'studying in the university',
	  					timetag: '16.00-17.00'},
	  				]
	  			},

	  			{
	  				time:'14/02/25 12:00-18:00',
	  				mood:'3',
	  				activities: [
	  					{description:'studying in the university', //list should be ordered by time
	  					timetag: '12.00-13.00'},

	  					{description:'studying in the university',
	  					timetag: '14.00-15.00'},

	  					{description:'studying in the university',
	  					timetag: '16.00-17.00'},
	  				]
	  			},

	  		],

	  		interval_24h:[
	  			{
	  				time:'14/02/25 12:00-18:00',
	  				mood:'5',
	  				activities: [
	  					{description:'studying in the university', //list should be ordered by time
	  					timetag: '12.00-13.00'},

	  					{description:'working',
	  					timetag: '14.00-15.00'},

	  					{description:'workout in gym',
	  					timetag: '16.00-17.00'},
	  				]
	  			},

	  			{
	  				time:'14/02/25 18:00-24:00',
	  				mood:'2',
	  				activities: [
	  					{description:'movie', //list should be ordered by time
	  					timetag: '18.00-19.00'},

	  					{description:'eating junk food',
	  					timetag: '19.00-20.00'},

	  					{description:'soialising',
	  					timetag: '20.00-21.00'},
	  				]
	  			},	  			

	  		],



	  };
  	//init

  		$s.currentIntervals=$s.data.interval_6h
			$log.log($s.displayInterval);
			$s.displayInterval=$s.data.interval_6h[0]
		//


  		$s.chooseInterval = function(interval){
  			$s.displayInterval=interval;
  		};
  		
  		$log.log($s.displayInterval.mood);



  		$s.getColor = function(interval){
  			if(interval.mood==5){
  			return "{backgroundColor:'#39E539'}";
  			};
  			if(interval.mood==4){
  			return "{backgroundColor:'#67E567'}";
  			}
  			if(interval.mood==3){
  			return "{backgroundColor:'#76FF9A'}";
  			};
  			if(interval.mood==2){
  			return "{backgroundColor:'#76FFC4'}";
  			};
  			if(interval.mood==1){
  			return "{backgroundColor:'#B4DFFF'}";
  			};

  		};

	}




]);