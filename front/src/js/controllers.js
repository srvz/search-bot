/**
 * Created on 10/12/15.
 */

const eventSearchInput = 'eventSearchInput';
const tipsTypeNone = 'none';
const tipsTypeMore = 'more';
const tipsTypeProgress = 'progress';
const tipsTypeMessage = 'message';


class MainController {
  constructor($rootScope, $scope, $routeParams, services) {

    this.$rootScope = $rootScope;
    this.$routeParams = $routeParams;
    this.services = services;

    this.params = new Map();
    this.results = new Map();
    this.types = new Map();

    this.showTips(tipsTypeNone);

    this.parseRouteParams();

    $scope.$on(eventSearchInput, this.handleEvent.bind(this));
  }

  handleEvent(event, args) {

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

      this.showTips(tipsTypeProgress);
      this.search();
    }
  }

  parseInput(input) {

    const q = input;
    if (q) {

      console.log('searching', input);
      this.params.clear();
      this.params.set('q', q);
      this.params.set('target', 'google');
      this.params.set('start', 0);
      this.params.set('type', 'web');
      this.params.set('rsz', 8);

      this.types.clear();
      this.results.clear();
      this.showTips(tipsTypeProgress);
      this.search();
    }
  }

  goNext() {

    const start = this.params.get('start');
    const rsz = this.params.get('rsz');
    this.params.set('start', start + rsz);
    this.showTips(tipsTypeProgress);
    this.search();
  }

  search() {

    this.showNoMore = false;
    this.showMoreCard = false;
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
        if (data.message) {

          if (this.results.size === 1) {
            this.noMoreMessage = 'No more results.'
          } else if (this.results.size === 0) {
            this.noMoreMessage = 'No results.'
          }
          this.showTips(tipsTypeMessage);
        } else {

          if (data.data) {

            let type = 'web';
            switch (data.type) {
              case 'images':
              case 'books':
              case 'video':
              case 'news':
                type = data.type;
                break;
              default :
                type = 'web';
                break;
            }

            if (this.types.get(type)) {

              let results = this.results.get(type);
              this.results.set(type, [...results, ...data.data.results])
            } else {
              this.types.clear();
              this.results.clear();
              this.types.set(type, true);
              this.results.set(type, data.data.results);
            }
            this.showTips(tipsTypeMore);
          }
        }
      })
      .catch((err) => {

        console.log(err);
        this.noMoreMessage = 'Something goes wrong.';
        this.showTips(tipsTypeMessage);
      })
  }

  showTips(type) {

    if (type === tipsTypeMore) {

      this.progressMode = null;
      this.showMoreCard = true;
      this.showMoreButton = true;
      this.showNoMore = false;
    } else if (type === tipsTypeProgress) {

      this.progressMode = 'indeterminate';
      this.showMoreCard = false;
      this.showMoreButton = false;
      this.showNoMore = false;
    } else if (type === tipsTypeMessage) {

      this.progressMode = null;
      this.showMoreCard = true;
      this.showMoreButton = false;
      this.showNoMore = true;
    } else if (type === tipsTypeNone){

      this.progressMode = null;
      this.showMoreCard = false;
      this.showMoreButton = false;
      this.showNoMore = false;
    }
  }
}


class HeaderController {
  constructor($rootScope, $scope, $routeParams) {

    this.$rootScope = $rootScope;
    this.data = {
      placeholder: '输入关键字搜索'
    };

    const q = $routeParams.q;
    if (q) {
      this.data.position = 'top';
      this.data.input = q;
    }
  }

  search() {

    this.$rootScope.$broadcast(eventSearchInput, this.data.input)
  }
}


class FooterController {
  constructor($scope, $mdDialog) {

    this.$mdDialog = $mdDialog;
    this.data = [
      '直接输入进行谷歌网页搜索，支持谷歌搜索规则，据谷歌API限制，最多返回64条结果',
      //'`!img` `!image` `!images` 搜索谷歌图片。例：`!img google`',
      //'`!video` 搜索谷歌视频。例：`!video google`',
      //'`!news` 搜索谷歌新闻',
      //'`!books` 搜索谷歌图书',
      '`!gh` `!github` 搜索 github.com。 例：`!gh google`',
      '`!so` `!sof` `!stackoverflow` 搜索 stackoverflow.com',
      '`!tw` `!twitter` 搜索 twitter.com',
      '`!wk` `!wiki` `!wikipedia` 搜索 wikipedia.com'
    ];
  }

  help(event) {

    let html = require('../jade/help.jade')();
    let icon = require('../assets/close_icon.svg');
    this.$mdDialog.show({
      controller: function($scope, $mdDialog, data, icon) {
        $scope.icon = icon;
        $scope.data = data;
        $scope.close = function() {
          $mdDialog.hide();
        }
      },
      template: html,
      parent: angular.element(document.body),
      targetEvent: event,
      clickOutsideToClose:true,
      locals: {
        icon: icon,
        data: this.data
      }
    }).then(function() {

    });
  }
}

MainController.$inject = ['$rootScope', '$scope', '$routeParams', 'services'];
HeaderController.$inject = ['$rootScope', '$scope', '$routeParams'];
FooterController.$inject = ['$scope', '$mdDialog'];

angular.module('Bot')
  .controller('MainController', MainController)
  .controller('HeaderController', HeaderController)
  .controller('FooterController', FooterController);
