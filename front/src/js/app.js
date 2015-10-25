/**
 * Created on 10/12/15.
 */

angular
  .module('Bot', ['ngRoute', 'ngResource', 'ngAria', 'ngAnimate', 'ngMaterial', 'ngSanitize'])
  .constant('host', window.location.origin)
  .run(runBlock);

runBlock.$inject = ['servicesConfigure'];
function runBlock(servicesConfigure) {

    servicesConfigure();
}