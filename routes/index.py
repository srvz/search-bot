from flask import Blueprint, render_template, request, send_from_directory
import os
from .weapons import get_logger

log = get_logger()

index = Blueprint('index', __name__)

@index.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(index.root_path, '../static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')

@index.route('/', methods=['GET', 'POST'])
def index_page():
    log.info('endpoint = %s', request.endpoint)
    log.info('headers = ', request.headers)
    log.info('values = ', request.values)
    log.info('args = ', request.args)
    log.info('view_args = ', request.view_args)
    log.info('environ = ', request.environ)
    return render_template('index.html')
