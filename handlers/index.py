import tornado.web
from jinja2 import Environment, PackageLoader
import os

env = Environment(loader=PackageLoader('handlers', '../templates'))
js_path = '/static/js/main.js'
if os.environ.get('PRODUCTION'):
    js_path = '/static/dist/main.min.js'
index_tpl = env.get_template('index.html').render(js_path=js_path)


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(index_tpl)
