'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
  controller('MyCtrl1', ['$scope', '$log', '$http', function($s, $log, $http) {

  		//mock data

  /*		$http.get('/someUrl').success(successCallback);{
  			$s.data=successCallback;
  		}
*/		$log.log($http.defaults.headers.common);
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
	  			}

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
	  				
	  					{description:'studying in the university', //list should be ordered by time
	  					timetag: '12.00-13.00'},

	  					{description:'working',
	  					timetag: '14.00-15.00'},

	  					{description:'workout in gym',
	  					timetag: '16.00-17.00'},
	  				
	  					{description:'studying in the university', //list should be ordered by time
	  					timetag: '12.00-13.00'},

	  					{description:'working',
	  					timetag: '14.00-15.00'},

	  					{description:'workout in gym',
	  					timetag: '16.00-17.00'},
	  				
	  					{description:'studying in the university', //list should be ordered by time
	  					timetag: '12.00-13.00'},

	  					{description:'working',
	  					timetag: '14.00-15.00'},

	  					{description:'workout in gym',
	  					timetag: '16.00-17.00'},
	  				
	  					{description:'studying in the university', //list should be ordered by time
	  					timetag: '12.00-13.00'},

	  					{description:'working',
	  					timetag: '14.00-15.00'},

	  					{description:'workout in gym',
	  					timetag: '16.00-17.00'},
	  				
	  					{description:'studying in the university', //list should be ordered by time
	  					timetag: '12.00-13.00'},

	  					{description:'working',
	  					timetag: '14.00-15.00'},

	  					{description:'workout in gym',
	  					timetag: '16.00-17.00'},
	  				
	  					{description:'studying in the university', //list should be ordered by time
	  					timetag: '12.00-13.00'},

	  					{description:'working',
	  					timetag: '14.00-15.00'},

	  					{description:'workout in gym',
	  					timetag: '16.00-17.00'},
	  				
	  					{description:'studying in the university', //list should be ordered by time
	  					timetag: '12.00-13.00'},

	  					{description:'working',
	  					timetag: '14.00-15.00'},

	  					{description:'workout in gym',
	  					timetag: '16.00-17.00'},
	  				
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

	  		]



	  };
$s.currentIntervals=[];
  		$s.create = function(size){
  			var lines=[size];
  			for (var i=0;i<size;i++){
  				lines[i]=["add Item here"];
  			$s.displayedLines=lines;
  			}
  		};

  		$s.chooseIntervalGrain = function(intervalGrain){
  			//  				$log.log(intervalGrain);
  		   	$s.currentIntervals=[];
  				var count=0;
  				for (var x in $s.data[intervalGrain]){
  				if (count==11) break
  				$s.currentIntervals.push($s.data[intervalGrain][x]);
  				count++;
  			}
  			$s.currentIntervals=$s.currentIntervals;
  		};

  	//init
  		$s.chooseIntervalGrain('interval_6h');
		$s.displayInterval=$s.data.interval_6h[0].acti;
		$s.intervalSize=6;
		$s.create($s.intervalSize);
		//


  		$s.chooseInterval = function(interval){
  			$s.displayInterval=interval;
  		};
  		


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


      
        
        $s.timeStringMood=function(date, time){
        	$log.log($s.date);
        	var theString="";
        	$log.log('1');
        	var x=date.replace(/-/g, "");        	$log.log('2');
        	var y=time.replace(/:/g, "");        	$log.log('3');
        	var z= x+y+"00";
        	$log.log(z);
        	return z;
        };
	
        $s.timeStringAction=function(date, time){
        	$log.log($s.date);
        	var theString="";$log.log('1');
        	var x=date.replace(/-/g, "");
        	var y=time.replace(/:/g, "");
        	var z= x+y;
        	$log.log(z);
        	return z;
        };

  		$s.submitMood = function(){
  	$log.log('1');
  			delete $http.defaults.headers.common['X-Requested-With'];
  			$log.log('sadsad');
  			var obj={
  				mood:$s.mood,
  				time:$s.timeStringMood($s.date1, $s.time1),
  				user:2
  			};
  			var x=angular.toJson(obj);
  			$log.log($http.defaults.headers);

			$http.post('http://localhost:5000/v0/add/mood', "obj", {
				headers: {
					   'Content-Type' : "application/x-www-form-urlencoded",
				}
                });
             };
  		$s.submitAction = function(){
  			var obj={
  				timeStart:$s.timeStringAction($s.date2, $s.time2),
  				timeStop:$s.timeStringAction($s.date3, $s.time3),
  				category:$s.category,
  				description:$s.text,
  				user:2
  			};
  			var x=angular.toJson(obj);
  			$log.log(x);

			$http.post('http://127.0.0.1:5000/v0/add/activity', obj, {
                headers: { 'Content-Type': undefined ,
            				'Access-Control-Allow-Origin':true},

                transformRequest: function(data) { return data; }
              }).success(function(data, status, headers, config) {

              }).
              error(function(data, status, headers, config) { 

          })};
}



]);
