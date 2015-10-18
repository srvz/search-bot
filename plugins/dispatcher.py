from plugins import google

def dispatch(options):

    target = options.get('target')
    if target == 'google':
        return google.fetch(options)
