app.controller('dashboardCtrl', function ($scope, $uibModal, $log, $http) {

  $http.get(host +'/api/get/top').success(function(data){
    $scope.cpu = data.cpu;
    $scope.mem = data.mem;
    $scope.mem.rate =  20;
//    document.querySelector('#memId').value=(data.mem.used/data.mem.total)* 100;
  })

});//---main ctrl end