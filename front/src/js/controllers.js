/**
 * Created on 10/12/15.
 */

const evtSearchInput = 'evtSearchInput';

class MainController {
  constructor($rootScope, $scope, $routeParams, services) {

    this.$rootScope = $rootScope;
    this.$routeParams = $routeParams;
    this.services = services;
    console.log('hello bot');
    this.params = new Map();
    this.parseRouteParams();

    $scope.$on(evtSearchInput, this.handleEvent.bind(this));
  }

  handleEvent(event, args) {

    console.log(event, args);
    this.parseInput(args);
  }

  parseRouteParams() {

    const params = this.$routeParams;
    console.log(params);
    const q = params.q;

    if (q) {

      this.params.set('q', q);
      this.params.set('target', params.target || 'google');
      this.params.set('start', params.start || 0);
      this.params.set('type', params.type || 'web');
      this.params.set('rsz', params.rsz || 8);

      this.search();
    }
  }

  parseInput(input) {

    const q = input;
    if (q) {

      console.log('searching', input);
      this.params.set('q', q);
      this.params.set('target', 'google');
      this.params.set('start', 0);
      this.params.set('type', 'web');
      this.params.set('rsz', 8);

      this.search();
    }
  }

  goNext() {

    const start = this.params.get('start');
    const rsz = this.params.get('rsz');
    this.params.set('start', start + rsz)
    this.search();
  }

  search() {

    console.log(this.params);
    let req = new this.services.Request({
      q: this.params.get('q'),
      target: this.params.get('target'),
      start: this.params.get('start'),
      type: this.params.get('type'),
      rsz: this.params.get('rsz')
    });

    req.$search()
      .then((data) => {

        console.log(data);
      })
      .catch((err) => {

        console.log(err);
      })
  }

}

class HeaderController {
  constructor($rootScope, $scope, $routeParams) {

    this.$rootScope = $rootScope;
    this.data = {
      placeholder: '请输入关键字或`!?`获取帮助'
    };

    const q = $routeParams.q;
    if (q) {
      this.data.position = 'top';
      this.data.input = q;
    }
  }

  search() {

    this.$rootScope.$broadcast(evtSearchInput, this.data.input)
  }
}

class FooterController {
  constructor($scope) {

  }

  help() {

    console.log('help!!!help!!!help!!!');
  }
}


angular.module('Bot')
  .controller('MainController', MainController)
  .controller('HeaderController', HeaderController)
  .controller('FooterController', FooterController);
