from plugins import google
from plugins import help as help_message


def dispatch(options):

    target = options.get('target')
    if target == 'google':
        return google.fetch(options)
    elif target == 'help':
        return {'data': help_message.data}


def wx_dispatch(options):

    target = options.get('target')
    if target == 'google':
        res = google.fetch(options)
        data = res.get('data', None)
        if data:
            results = data.get('results', None)
            type = data.get('type', '')
            if type == 'web':
                rst = ''
                counter = 0
                for item in results:
                    counter += 1
                    rst += counter + '.'
                    rst += item['titleNoFormatting'] + '\n'
                    rst += item['content'] + '\n'
                    rst += item['unescapedUrl'] + '\n'
                return rst
            elif type == 'images':
                pass
        return res.get('message', 'No results.')
    elif target == 'help':
        return '\n'.join(help_message.data)
