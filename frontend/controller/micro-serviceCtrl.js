app.controller('microServiceCtrl', function ($scope, $uibModal, $log, $http) {

  $http.get(host+"/api/service/info").success(function(data){
    $scope.jarInfo = data;
  })

  $http.get(host+"/api/running/service/info").success(function(data){
    $scope.runningServiceInfo = data;
  })

  $scope.animationsEnabled = true;

  $scope.openPostJarFileForm = function () {
    var modalInstance = $uibModal.open({
      animation: $scope.animationsEnabled,
      templateUrl: 'postJarFileTable.html',
      controller: 'postJarFileTableCtrl',
      size: 'lg'
    });
    modalInstance.result.then(function (selectedItem) {
      $scope.selected = selectedItem;
    }, function () {
      $log.info('Modal dismissed at: ' + new Date());
    });

    $scope.toggleAnimation = function () {
      $scope.animationsEnabled = !$scope.animationsEnabled;
    };
  };

  $scope.openServiceInfo = function (id) {

    var modalInstance = $uibModal.open({
      animation: $scope.animationsEnabled,
      templateUrl: 'serviceInfoTable.html',
      controller: 'serviceInfoTableCtrl',
      size: 'lg',
      resolve: {
        serviceId: function () {
          return id;
        }
      }
    });
    modalInstance.result.then(function (selectedItem) {
      $scope.selected = selectedItem;
    }, function () {
      $log.info('Modal dismissed at: ' + new Date());
    });

    $scope.toggleAnimation = function () {
      $scope.animationsEnabled = !$scope.animationsEnabled;
    };
  };

  $scope.openEnvServiceInfo = function (id) {

    var modalInstance = $uibModal.open({
      animation: $scope.animationsEnabled,
      templateUrl: 'serviceEnvInfoTable.html',
      controller: 'runningServiceEnvInfoTableCtrl',
      size: 'lg',
      resolve: {
        serviceId: function () {
          return id;
        }
      }
    });
    modalInstance.result.then(function (selectedItem) {
      $scope.selected = selectedItem;
    }, function () {
      $log.info('Modal dismissed at: ' + new Date());
    });

    $scope.toggleAnimation = function () {
      $scope.animationsEnabled = !$scope.animationsEnabled;
    };
  };

});//---main ctrl end

app.controller('postJarFileTableCtrl', function ($scope, $uibModalInstance, $http) {

  $scope.ok = function () {
    $uibModalInstance.close($scope.selected.item);
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
});

app.controller('serviceInfoTableCtrl', function ($scope, $uibModalInstance, $http, serviceId) {
  url=host+"/api/running/service/detail/info?id="+serviceId;
  $http.get(url).success(function(data){
  $scope.serviceDetailInfo = data;
  })
  $scope.testStr = serviceId;
  $scope.serviceName = serviceId;
  $scope.selected = {
    serviceName: $scope.serviceName
  };

  $scope.ok = function () {
    $uibModalInstance.close($scope.selected.serviceName);
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
});

app.controller('runningServiceEnvInfoTableCtrl', function ($scope, $uibModalInstance, $http, serviceId) {
   url=host+"/api/running/service/env/info?id="+serviceId;
  $http.get(url).success(function(data){
  $scope.runningServiceEnvInfo = data;
  })
  $scope.testStr = serviceId;
  $scope.serviceName = serviceId;
  $scope.selected = {
    serviceName: $scope.serviceName
  };

  $scope.ok = function () {
    $uibModalInstance.close($scope.selected.serviceName);
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
});