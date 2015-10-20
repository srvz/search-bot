from plugins import google
from plugins import help as help_message

def dispatch(options):

    target = options.get('target')
    if target == 'google':
        return google.fetch(options)
    elif target == 'help':
        return {'data': help_message.data}
