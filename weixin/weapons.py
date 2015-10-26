import logging
import os
import hashlib
from .config import appid, appsecret, wx_token
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

log = get_logger('weixin')


def parse_query(query):
    args = {
        'target': 'google',
        'start':  0,
        'rsz':  8,
        'type': 'web',
        'q': query
    }
    query = query.strip()
    if query.startswith('!'):
        index = query.find(' ')
        if index > -1:
            keyword = query[1:index]
            if keyword in ['?', 'help']:
                args['target'] = keyword
            else:
                args['type'] = keyword
            args['q'] = query[index + 1:]
        else:
            keyword = query[1:]
            if keyword in ['?', 'help']:
                args['target'] = keyword

    log.info('parse args = %s', args)
    return args


def verify_wechat(signature, timestamp, nonce):
    tmp_list = [timestamp, nonce, wx_token]
    joined = ''.join(sorted(tmp_list))
    byted = bytes(joined, encoding='utf8')
    hexed = hashlib.sha1(byted).hexdigest()
    if hexed == signature:
        return True
    return False


def get_access_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token'
    params = {
        'grant_type': 'client_credential',
        'appid': appid,
        'secret': appsecret
    }
    return GET(url, params)
