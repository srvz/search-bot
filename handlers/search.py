import tornado.web
from tornado import gen
from tornado.gen import Future
from .weapons import get_logger
from plugins.dispatcher import dispatch

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

    def parse_args(self, method='GET'):

        get_argument = self.get_query_argument
        if method == 'POST':
            get_argument = self.get_body_argument

        query = get_argument('q', '')
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
