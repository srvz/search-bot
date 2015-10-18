import tornado.web
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('handlers', '../templates'))
index_tpl = env.get_template('index.html').render()

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(index_tpl)
