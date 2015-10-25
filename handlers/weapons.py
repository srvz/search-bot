import logging
import os
import hashlib
from plugins.weapons import get as GET

def get_logger(name='handlers', level=logging.DEBUG):
    if os.environ.get('PRODUCTION'):
        level = logging.CRITICAL
    format_tpl = (
        '%(asctime)s|%(levelname)s|'
        '%(name)s:%(module)s:%(funcName)s:%(lineno)s >>> %(message)s'
    )
    logging.basicConfig(format=format_tpl)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger


def verify_wechat(signature, timestamp, nonce, token):
    tmp_list = [timestamp, nonce, token]
    joined = ''.join(sorted(tmp_list))
    byted = bytes(joined, encoding='utf8')
    hexed = hashlib.sha1(byted).hexdigest()
    if hexed == signature:
        return True
    return False

appid = 'wx03373c7dab1a0d4c'
appsecret = '6d7d1481adb8d84be1c5e007f5c822f8'
def get_access_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token'
    params = {
        'grant_type': 'client_credential',
        'appid': appid,
        'secret': appsecret
    }
    return GET(url, params)
