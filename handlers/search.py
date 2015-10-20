import tornado.web
from tornado import gen
from tornado.gen import Future
from .weapons import get_logger
from plugins.dispatcher import dispatch
import json

log = get_logger()

class SearchHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        args = self.parse_args()
        rst = yield self.fetch(args)
        self.write(rst)

    @gen.coroutine
    def post(self):
        args = self.parse_args('POST')
        rst = yield self.fetch(args)
        self.write(rst)

    @staticmethod
    def fetch(args):
        future = Future()
        future.set_result(dispatch(args))
        return future

    def cx_get_body_argument(self, name, default=''):
        try:
            body = {}
            if isinstance(self.request.body, str):
                body = json.loads(self.request.body)
            elif isinstance(self.request.body, bytes):
                body = json.loads(self.request.body.decode(encoding='utf-8'))

            if isinstance(body, dict):
                return body.get(name, default)
        except Exception as e:
            log.error('err %s', e)
        return default

    def parse_args(self, method='GET'):

        get_argument = self.get_argument
        if method == 'POST':
            get_argument = self.cx_get_body_argument

        query = get_argument('q', '')
        log.info('query %s , %s , %s', query, get_argument, self.request.body)
        args = {
            'target': get_argument('target', 'google'),
            'start': get_argument('start', 0),
            'rsz': get_argument('rsz', 8),
            'type': get_argument('type', 'web'),
            'q': query
        }
        query = query.strip()
        if query.startswith('!'):
            index = query.find(' ')
            if index > -1:
                keyword = query[1:index]
                if keyword in ['?']:
                    args['target'] = keyword
                else:
                    args['type'] = keyword
                args['q'] = query[index + 1:]

        log.info('parse args = %s', args)
        return args
