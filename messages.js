angular.module('messages', ['ngAnimate', 'ui.bootstrap']);

angular.module('messages').config(function($httpProvider){
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});

angular.module('messages').controller('messagesCtrl', function ($scope, $uibModal, $log, $http) {


});//---main ctrl end
