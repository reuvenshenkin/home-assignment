// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
angular.module('starter', ['ionic'])
.factory('questionService', function($http) {
  return {
    getQuestions: function(){
      return $http.get('https://localhost:8000/questions/').then(function(response){
        return response.data.questions;
      });
    }
  }
})

.controller("MainCtrl",function($scope, questionService){
  questionService.getQuestions().then(function(questions){
    $scope.questions = questions;
  });
})
.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    if(window.cordova && window.cordova.plugins.Keyboard) {
      // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
      // for form inputs)
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);

      // Don't remove this line unless you know what you are doing. It stops the viewport
      // from snapping when text inputs are focused. Ionic handles this internally for
      // a much nicer keyboard experience.
      cordova.plugins.Keyboard.disableScroll(true);
    }
    if(window.StatusBar) {
      StatusBar.styleDefault();
    }
  });
})

.factory('questionService', function($http) {
  return {
    getQuestions: function(){
      return $http.get('https://localhost\\:8000/questions/').then(function(response){
        return response.data.questions;
      });
    }
  }
})

.controller("MainCtrl",function($scope, questionService){
  questionService.getQuestions().then(function(questions){
    $scope.questions = questions;
  });
})

.config(function($stateProvider, $urlRouterProvider){
  $stateProvider

  .state('main', {
    url: "/main",
    templateUrl: "templates/main.html",
    controller: 'MainCtrl'
  })

  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/main');
});