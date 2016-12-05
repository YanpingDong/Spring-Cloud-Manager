angular.module('index', ['ngAnimate', 'ui.bootstrap']);

angular.module('index').config(function($httpProvider){
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});

angular.module('index').controller('indexCtrl', function ($scope, $uibModal, $log, $http) {

  $http.get("http://localhost:8000/api/get/top").success(function(data){
    $scope.cpu = data.cpu;
    $scope.mem = data.mem;
    $scope.mem.rate =  20;
//    document.querySelector('#memId').value=(data.mem.used/data.mem.total)* 100;
  })

});//---main ctrl end