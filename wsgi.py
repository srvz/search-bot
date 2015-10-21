from tornado.wsgi import WSGIApplication
import os
from handlers.index import MainHandler
from handlers.search import SearchHandler


if __name__ == '__main__':

    settings = {
        'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        'name': __name__,
    }
    app = WSGIApplication([
        (r'/', MainHandler),
        (r'/api/search', SearchHandler)
    ], **settings)

    ip = 'localhost'
    port = 8051

    from wsgiref.simple_server import make_server
    httpd = make_server(ip, port, app)
    httpd.serve_forever()
