import tornado.web
from tornado import gen
from tornado.gen import Future
from .weapons import get_logger, verify_wechat
from plugins.dispatcher import dispatch
import json
from .config import wx_token

log = get_logger()

class WechatHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):

        echoStr = self.get_query_argument('echostr', '')
        verified = self.verify_url()
        log.info('verified %s', verified)
        log.ingo('request body %s', self.request.body)
        if verified:
            self.write(echoStr)
        else:
            self.write(echoStr)

    def verify_url(self):
        signature = self.get_query_argument('signature', '')
        timestamp = self.get_query_argument('timestamp', '')
        nonce = self.get_query_argument('nonce', '')
        return verify_wechat(signature, timestamp, nonce, wx_token)

    def post(self, *args, **kwargs):
        log.info('request body %s', self.request.body)
        self.write('')
