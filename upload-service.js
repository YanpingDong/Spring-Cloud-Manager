angular.module('uploadService', ['ngAnimate', 'ui.bootstrap']);

angular.module('uploadService').config(function($httpProvider){
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});

angular.module('uploadService').controller('uploadServiceCtrl', function ($scope, $uibModal, $log, $http) {
    $scope.save = function() {
          var fd = new FormData();
          var file = document.querySelector('input[type=file]').files[0];
          fd.append('file', file);
          $http({
               method:'POST',
               url:"http://10.120.137.175:5000/service/upload",
               data: fd,
               headers: {'Content-Type':undefined},
                transformRequest: function(data){
                var formData = new FormData();
                formData.append('file',data.file)
              }
               }).success( function ( response )
                       {
                       alert("uplaod success");
                       });
     }
});//---main ctrl end