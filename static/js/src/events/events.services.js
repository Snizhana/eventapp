'use strict'

angular
    .module('eventapp.events.services', [])
    .factory('EventsList', EventsList);

EventsList.$inject = ['$http']

function EventsList($http){
    function getEventsList(){
        return $http({
          method : "GET",
          url : 'api/events/'
        });
    }

    function getEvent(id){
        return $http({
          method : "GET",
          url : 'api/events/' + id
        });
    }

    function register(data, config){
        return $http.post('api/application/', data, config)
    }

    return{
        getEventsList: getEventsList,
        getEvent: getEvent,
        register: register
    }
};
