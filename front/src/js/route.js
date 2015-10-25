
angular.module('Bot')
  .config(config);

config.$inject = ['$routeProvider', '$locationProvider'];
function config($routeProvider, $locationProvider) {

  function templateWithName(name) {

    return require(`../jade/${name}.jade`)
  }

  let main = {
      template: templateWithName('main'),
      controller: 'MainController',
      controllerAs: 'main'
  };

  $routeProvider.when('/', main)
    .when('/search', main)
    .otherwise({
			redirectTo: '/'
		});

  $locationProvider.html5Mode(true);
}
