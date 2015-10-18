/**
 * Created on 10/12/15.
 */

Request.$inject = ['$resource', 'host'];
function Request($resource, host) {

  return $resource(host + '/api/search', {}, {
    search: {
      method: 'POST'
    }
  });
}

servicesConfigure.$inject = ['services', 'Request'];
function servicesConfigure(services, Request) {

  return () => {
    services.Request = Request;
  }
}

angular.module('Bot')
  .constant('services', {})
  .factory('Request', Request)
  .factory('servicesConfigure', servicesConfigure);