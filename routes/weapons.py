import logging

def get_logger(name='routes', level=logging.DEBUG):
    format_tpl = (
        '%(asctime)s|%(levelname)s|'
        '%(name)s:%(module)s:%(funcName)s:%(lineno)s >>> %(message)s'
    )
    logging.basicConfig(format=format_tpl)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger

log = get_logger()

def parse_request_params(params):
    query = params.get('q', '')
    args = {
        'target': params.get('target', 'google'),
        'start': params.get('start', 0),
        'rsz': params.get('rsz', 8),
        'type': params.get('type', 'web'),
        'q': query
    }

    query = query.strip()
    if query.startswith('!'):
        index = query.find(' ')
        if index > -1:
            args['type'] = query[1:index]
            args['q'] = query[index + 1:]

    log.info('args = %s', args)
    return args


