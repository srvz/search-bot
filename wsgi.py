from tornado.wsgi import WSGIApplication
import os
import sys
from handlers.index import MainHandler
from handlers.search import SearchHandler


if __name__ == '__main__':

    sys.path.insert(0, os.path.dirname(__file__))
    virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
    os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python3.3/site-packages')
    virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
    try:
        exec(compile(open(virtualenv).read(), virtualenv, 'exec'), dict(__file__=virtualenv))
        exec_namespace = dict(__file__=virtualenv)
        with open(virtualenv, 'rb') as exec_file:
            file_contents = exec_file.read()
        compiled_code = compile(file_contents, virtualenv, 'exec')
        exec(compiled_code, exec_namespace)
    except IOError:
        pass

    # if 'OPENSHIFT_REPO_DIR' in os.environ:
    #     settings = {
    #         'static_path': os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'static'),
    #         'name': 'bot',
    #     }
    # else:
    settings = {
        'static_path': os.path.join(os.getcwd(), 'static'),
        'name': 'bot',
    }
    app = WSGIApplication([
        (r'/', MainHandler),
        (r'/api/search', SearchHandler)
    ], **settings)

    ip = os.environ['OPENSHIFT_PYTHON_IP']
    port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
    host_name = os.environ['OPENSHIFT_GEAR_DNS']

    from wsgiref.simple_server import make_server
    httpd = make_server(ip, port, app)
    httpd.serve_forever()
