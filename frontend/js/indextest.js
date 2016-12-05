var indexApp = angular.module('myApp', []);

indexApp.config(function($httpProvider){
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});


//indexApp.controller('myCtrl', function($scope, $http) {
//    $scope.firstName = "John";
//    $scope.lastName = "Doe";
//    $scope.errorMessage = "no error";
//    $http.defaults.useXDomain = true;
//    $http.get('http://localhost:8000/api/mytest',
//           {headers:{'Access-Control-Allow-Origin':'*',
//           'Access-Control-Allow-Methods':'GET, POST, PUT, DELETE'}})
//    .success(function(data,status,headers,config){
//        $scope.message = data;
//        $scope.errorMessage = "no error";
//    }).error(function(data, status, headers,config){
//        $scope.message = data;
//        $scope.errorMessage = "xxxerror";
//    });
//});

indexApp.controller('myCtrl', function($scope, $http) {
    $http.get("http://localhost:8000/api/mytest").success(function(data){$scope.message = data.sites;})
});