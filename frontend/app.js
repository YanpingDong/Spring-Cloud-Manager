var app = angular.module('SpringCloudManager', ['ui.router','ngAnimate', 'ui.bootstrap']);

app.config(function($httpProvider){
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});

app.config(function($stateProvider) {
  var dashboardState = {
    name: 'dashboard',
    url: 'dashboard',
    templateUrl: 'view/dashboard.html',
    controller:'dashboardCtrl'
  }

  var microServiceState = {
    name: 'microService',
    url: 'microService',
    templateUrl: 'view/micro-service.html'
  }

  var uploadServiceState = {
    name: 'uploadService',
    url: 'uploadService',
    templateUrl: 'view/upload-service.html'
  }

  var messagesState = {
    name: 'messages',
    url: 'messages',
    templateUrl: 'view/messages.html'
  }

  $stateProvider.state(dashboardState);
  $stateProvider.state(microServiceState);
  $stateProvider.state(uploadServiceState);
  $stateProvider.state(messagesState);
});