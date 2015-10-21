from tornado.wsgi import WSGIApplication
import os
import sys
from handlers.index import MainHandler
from handlers.search import SearchHandler

sys.path.insert(0, os.path.dirname(__file__))
virtenv = os.environ.get('OPENSHIFT_PYTHON_DIR', os.getcwd()) + '/virtenv/'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python3.3/site-packages')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    exec (compile(open(virtualenv).read(), virtualenv, 'exec'), dict(__file__=virtualenv))
    exec_namespace = dict(__file__=virtualenv)
    with open(virtualenv, 'rb') as exec_file:
        file_contents = exec_file.read()
    compiled_code = compile(file_contents, virtualenv, 'exec')
    exec (compiled_code, exec_namespace)
except IOError:
    pass

settings = {
    'static_path': os.path.join(os.getcwd(), 'static'),
    'name': 'bot',
}

application = WSGIApplication([
    (r'/', MainHandler),
    (r'/api/search', SearchHandler)
], **settings)

if __name__ == '__main__':

    from wsgiref.simple_server import make_server

    ip = os.environ.get('OPENSHIFT_PYTHON_IP', 'localhost')
    port = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 8051))
    httpd = make_server(ip, port, application)
    httpd.serve_forever()
