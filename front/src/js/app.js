/**
 * Created on 10/12/15.
 */

angular
  .module('Bot', ['ngRoute', 'ngResource', 'ngAria', 'ngAnimate', 'ngMaterial', 'ngSanitize'])
  .constant('host', 'http://127.0.0.1:5080')
  .run(runBlock);

runBlock.$inject = ['servicesConfigure'];
function runBlock(servicesConfigure) {

    servicesConfigure();
}