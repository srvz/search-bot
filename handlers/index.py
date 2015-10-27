import tornado.web
from jinja2 import Environment, PackageLoader
import os

env = Environment(loader=PackageLoader('handlers', '../templates'))

js_path = '/static/js/main.js'
if os.environ.get('PRODUCTION') == '1':
    js_path = 'http://7xnocn.com1.z0.glb.clouddn.com/main.min.js'
else:
    pass
    # js_path = '/static/dist/main.min.js'

index_tpl = env.get_template('index.html').render(js_path=js_path)


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(index_tpl)
