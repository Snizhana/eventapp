'use strict';

angular
  .module('eventapp.events.controllers', [])
  .controller('EventsController', EventsController)
  .controller('EventDetailController', EventDetailController);

  EventsController.$inject = ['$scope', 'EventsList'];
  EventDetailController.$inject = ['$scope', '$stateParams', 'EventsList'];

  function EventsController($scope, EventsList){

    EventsList.getEventsList().then(function(response) {
          $scope.events = response.data;
        });
  }


  function EventDetailController($scope, $stateParams, EventsList){

    $scope.isSummitted = false;

    $scope.config = {
      headers: {'Content-Type': undefined },
      transformRequest: transformImageRequest
    }

    $scope.registrationData = {
      event_id: $stateParams.id
    }

    EventsList.getEvent($stateParams.id).then(function(response) {
          $scope.event = response.data;
        });

    function transformImageRequest(data) {
      var fd = new FormData();
      angular.forEach(data, function(value, key) {
        if (value instanceof FileList) {
          if (value.length === 1) {
            fd.append(key, value[0]);
          } else {
            angular.forEach(value, function(file, index) {
              fd.append(key + '_' + index, file);
            });
          }
        } else {
          fd.append(key, value);
        }
      });
      return fd;
    }

    $scope.uploadFile = function(files){
      $scope.registrationData["user_image"] = files;
    }

    $scope.register = function(data, config){
      EventsList.register(data, config).then(function(response) {
            $scope.isSummitted = true;
            $scope.registrationData = {};
          });
    }

  }
