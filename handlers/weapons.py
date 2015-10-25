import logging
import os
import hashlib

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
    sorted_list = [timestamp, nonce, token].sort()
    joined = ''.join(sorted_list)
    byted = bytes(joined, encoding='utf8')
    hexed = hashlib.sha1(byted).hexdigest()

    if hexed == signature:
        return True
    return False
