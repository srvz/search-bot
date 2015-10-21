from flask import Blueprint, abort, request, jsonify
from .weapons import parse_request_params
from plugins.dispatcher import dispatch

search = Blueprint('search', __name__, url_prefix='/api')


@search.route('/search', methods=['GET', 'POST'])
def api_search():
    if request.method in ['GET', 'POST']:
        rst = dispatch(parse_request_params(request.values))
        if rst.get('data'):
            return jsonify(rst['data'])
        else:
            return jsonify(rst)
    abort(405)
    return jsonify(parse_request_params(request.values))
