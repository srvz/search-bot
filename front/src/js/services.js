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

changeTitle.$inject = ['$rootScope'];
function changeTitle($rootScope) {
  return (title) => {
    $rootScope.title = title
  }
}

servicesConfigure.$inject = ['services', 'Request', 'changeTitle'];
function servicesConfigure(services, Request, changeTitle) {

  return () => {
    services.Request = Request;
    services.changeTitle = changeTitle;
  }
}

angular.module('Bot')
  .constant('services', {})
  .factory('Request', Request)
  .factory('changeTitle', changeTitle)
  .factory('servicesConfigure', servicesConfigure);