import json
import tornado.web
from tornado import gen
from tornado.gen import Future
from plugins.dispatcher import wx_dispatch
from weixin.weapons import verify_wechat, parse_query
from weixin.wxmessage import parse_message_body, text_message
from .weapons import get_logger

log = get_logger()

class WechatHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):

        echoStr = self.get_query_argument('echostr', '')
        verified = self.verify_url()
        log.info('verified %s', verified)
        log.info('query arguments %s', self.request.query_arguments)
        if verified:
            self.write(echoStr)
        else:
            self.write(echoStr)

    def verify_url(self):
        signature = self.get_query_argument('signature', '')
        timestamp = self.get_query_argument('timestamp', '')
        nonce = self.get_query_argument('nonce', '')
        return verify_wechat(signature, timestamp, nonce)

    @gen.coroutine
    def post(self, *args, **kwargs):

        log.info(self.request.body)
        log.info(self.request.query_arguments)
        self.parse_post_args()

    def parse_post_args(self):
        if len(self.request.query_arguments) and self.get_query_argument('encrypt_type', None):
            msg_signature = self.get_query_argument('msg_signature', None)
            signature = self.get_query_argument('signature', None)
            timestamp = self.get_query_argument('timestamp', None)
            nonce = self.get_query_argument('nonce', None)
            encrypt_type = self.get_query_argument('encrypt_type', None)
            if encrypt_type == 'aes':
                pass
            self.write('')
        else:
            params = parse_message_body(self.request.body)
            if params['MsgType'] == 'text':
                args = parse_query(params['Content'])
                response = yield self.compose_message(params['FromUserName'], params['ToUserName'], args)
                log.info('response type %s', type(response))
                self.write(response)
            else:
                self.write('')

    @staticmethod
    def compose_message(to_user, from_user, args):
        future = Future()
        future.set_result(text_message(to_user, from_user, wx_dispatch(args)))
        return future

