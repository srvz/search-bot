/**
 * Created on 10/14/15.
 */

const DOCUMENT = new WeakMap();
class SearchBox {
  constructor($document) {

    this.restrict = 'E';
    this.scope = {
      data: '=sbData',
      search: '&sbSearch'
    };
    this.template = require('../jade/searchbox.jade');
    DOCUMENT.set(this, $document)
  }

  link(scope, elem) {

    changePosition();

    const form = angular.element(elem.find('form')[0]);

    form.on('keyup', function(e) {

      if (e && e.which === 13) {

        form[0].submit();
      }
    });

    var deregister = scope.$watch('data.input', function(newCalue, oldValue) {

      if (scope.data.position === 'top' || scope.data.position === 'keep') {

        changePosition();
        deregister();
      }
    });

    function changePosition() {

      if (scope.data.position === 'keep') {

        return;
      }

      const $document = DOCUMENT.get(SearchBox.instance);
      const height = ($document[0].body.clientHeight - 38) * 0.38;
      const searchbox = angular.element(elem.children()[0]);

      if (!scope.data.position || scope.data.position === 'middle') {

        searchbox.css({top: height + 'px'});
      } else if (scope.data.position === 'top') {

        searchbox.css({top: '10px'});
        scope.data.position = 'keep';
      }
    }
  }

  static directiveFactory($document) {
    SearchBox.instance = new SearchBox($document);
    return SearchBox.instance;
  }
}

SearchBox.directiveFactory.$inject = ['$document'];

angular.module('Bot')
  .directive('searchbox', SearchBox.directiveFactory);
