angular.module('microService', ['ngAnimate', 'ui.bootstrap']);
angular.module('microService').controller('microServiceCtrl', function ($scope, $uibModal, $log) {

  $scope.items = ['item1', 'item2', 'item3'];

  $scope.animationsEnabled = true;

  $scope.openPostJarFileForm = function (size) {

    var modalInstance = $uibModal.open({
      animation: $scope.animationsEnabled,
      templateUrl: 'postJarFileTable.html',
      controller: 'postJarFileTableCtrl',
      size: size,
      resolve: {
        items: function () {
          return $scope.items;
        }
      }
    });

    modalInstance.result.then(function (selectedItem) {
      $scope.selected = selectedItem;
    }, function () {
      $log.info('Modal dismissed at: ' + new Date());
    });
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
  };

  $scope.toggleAnimation = function () {
    $scope.animationsEnabled = !$scope.animationsEnabled;
  };

});

angular.module('microService').controller('postJarFileTableCtrl', function ($scope, $uibModalInstance, items) {

  $scope.items = items;
  $scope.selected = {
    item: $scope.items[0]
  };

  $scope.ok = function () {
    $uibModalInstance.close($scope.selected.item);
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
});

angular.module('microService').controller('serviceInfoTableCtrl', function ($scope, $uibModalInstance, serviceId) {
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