angular.module('uploadService', ['ngAnimate', 'ui.bootstrap']);

angular.module('uploadService').config(function($httpProvider){
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});

angular.module('uploadService').controller('uploadServiceCtrl', function ($scope, $uibModal, $log, $http) {
    $scope.save = function() {
          var formData = new FormData();
          var file = document.querySelector('input[type=file]').files[0];
          var name = $scope.name;
          var date = document.querySelector('#date').value;
          var version = $scope.version;
          var userId = $scope.userId;
          var description = document.querySelector('#textarea').value;
          formData.append('name', name);
          formData.append('file', file);
          formData.append('date', date);
          formData.append('version', version);
          formData.append('userId', userId);
          $http({
               method:'POST',
               url:"http://10.120.137.175:5000/service/upload",
               data: formData,
               headers: {'Content-Type':undefined}
               }).success( function ( response )
                       {
                       alert("uplaod success");
                       });
     }
});//---main ctrl end