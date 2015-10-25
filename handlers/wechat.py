import tornado.web
from tornado import gen
from tornado.gen import Future
from .weapons import get_logger, verify_wechat
from plugins.dispatcher import dispatch
import json
from .config import wx_token
import schedule
import time

log = get_logger()
# access_token = ''
# def cron_job():
#     access_token = 'some token'
#     log.info('access_token %s', access_token)
#
# schedule.every(7000).seconds.do(cron_job)
# while 1:
#     schedule.run_pending()
#     time.sleep(500)

class WechatHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):

        echoStr = self.get_query_argument('echostr', '')
        verified = self.verify_url()
        log.info('verifid %s', verified)
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
