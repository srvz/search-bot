import requests
import logging
import os


def get_logger(name='plugins', level=logging.DEBUG):

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

log = get_logger()


def get(url, params):
    try:
        req = requests.get(url, params=params, timeout=3)
        log.info('get url = %s', req.url)
        if req.ok:
            return req.content
        else:
            log.info('request not ok %s %s', req.reason, req.content)
    except Exception as e:
        log.error('request exception = %s', e)
    return None

