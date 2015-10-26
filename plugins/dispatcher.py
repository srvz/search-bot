from plugins import google
from plugins import help as help_message
from .weapons import get_logger
import html

log = get_logger()


def dispatch(options):

    target = options.get('target')
    if target == 'google':
        return google.fetch(options)
    elif target in ['?', 'help']:
        return {'data': help_message.data}


def wx_dispatch(options):

    target = options.get('target')
    if target == 'google':
        res = google.fetch(options)
        data = res.get('data', None)
        log.info('data %s', data)
        if data:
            results = data.get('results', None)
            m_type = res.get('type', '')
            if m_type in ['web', 'github', 'stackoverflow', 'twitter', 'wikipedia', 'zhihu', 'v2ex']:
                rst = ''
                counter = 0
                for item in results:
                    counter += 1
                    rst += str(counter) + '. '
                    rst += html.unescape(item['titleNoFormatting']) + '\n'
                    # rst += item['content'] + '\n'
                    rst += item['unescapedUrl'] + '\n\n'
                return rst
            elif m_type == 'images':
                pass
        return res.get('message', 'No results.')
    elif target in ['?', 'help']:
        return '\n'.join(help_message.data)
