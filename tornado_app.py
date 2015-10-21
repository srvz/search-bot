from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.web import Application
import os
from handlers.index import MainHandler
from handlers.search import SearchHandler


settings = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'name': __name__,
}
app = Application([
    (r'/', MainHandler),
    (r'/api/search', SearchHandler)
], **settings)


def main():
    server = HTTPServer(app)
    server.bind(os.environ.get('PORT', 5080))
    server.start(0)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
