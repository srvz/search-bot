from .weapons import get, get_logger
import json

log = get_logger()

def fetch(args):

    log.info('fetch args %s', args)
    search_type = args.get('type')
    if search_type == 'web':
        rst = web(args)
    elif search_type in ['img', 'image', 'images']:
        rst = images(args)
    elif search_type == 'video':
        rst = video(args)
    elif search_type == 'news':
        rst = news(args)
    elif search_type == 'books':
        rst = books(args)
    elif search_type in ['gh', 'github']:
        rst = github(args)
    elif search_type in ['so', 'sof', 'stackoverflow']:
        rst = stackoverflow(args)
    elif search_type in ['tw', 'twitter']:
        rst = twitter(args)
    elif search_type in ['wk', 'wiki', 'wikipedia']:
        rst = wikipedia(args)
    elif search_type in ['zh', 'zhihu']:
        rst = zhihu(args)
    elif search_type in ['sf', 'segmentfault']:
        rst = segmentfault(args)
    elif search_type in ['v2', 'v2ex']:
        rst = v2ex(args)
    else:
        rst = web(args)

    if rst:
        if isinstance(rst, bytes):
            rst_str = rst.decode(encoding='utf-8')
            return {'data': json.loads(rst_str), type: search_type}
        elif isinstance(rst, str):
            return {'data': json.loads(rst), type: search_type}
        return {'data': rst, type: search_type}
    return {'message': 'No result.'}

def compose_url(serach_scope):
    base_url = 'https://ajax.googleapis.com/ajax/services/search/'
    return base_url + serach_scope

def compose_params(args):
    params = {
        'v': 1.0,
        'start': args.get('start', 0),
        'rsz': args.get('rsz', 8),
        'q': args.get('q', '')
    }
    return params

def get_web(args):
    return get(compose_url('web'), args)

def web(args):
    return get_web(compose_params(args))

def images(args):
    return get(compose_url('images'), compose_params(args))

def video(args):
    return get(compose_url('video'), compose_params(args))

def news(args):
    return get(compose_url('news'), compose_params(args))

def books(args):
    return get(compose_url('books'), compose_params(args))

def github(args):
    args['q'] = args.get('q') + ' site:github.com'
    return get_web(compose_params(args))

def stackoverflow(args):
    args['q'] = args.get('q') + ' site:stackoverflow.com'
    return get_web(compose_params(args))

def twitter(args):
    args['q'] = args.get('q') + ' site:twitter.com'
    return get_web(compose_params(args))

def wikipedia(args):
    args['q'] = args.get('q') + ' site:wikipedia.org'
    return get_web(compose_params(args))

def zhihu(args):
    args['q'] = args.get('q') + ' site:zhihu.com'
    return get_web(compose_params(args))

def segmentfault(args):
    args['q'] = args.get('q') + ' site:segmentfault.com'
    return get_web(compose_params(args))

def v2ex(args):
    args['q'] = args.get('q') + ' site:v2ex.com'
    return get_web(compose_params(args))
