from flask import Flask, request, render_template
import json
import requests

app = Flask(__name__)

google_search_api = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&start=0&rsz=8&q='

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():

    print request.values
    if request.method == 'GET':

        rst = search_google(request)
        t = safe_get(request.args, 't')
        q = safe_get(request.args, 'q');
        print 't = ', t, 'q = ', q
        if rst:
            if t is None:
                return rst
            else:
                return render_template('results.html', title=q, results=rst)
        else:
            return 'No Results.'
    else:
        return 'Invalid request method.'


def safe_get(collections, key):
    try:
        return collections[key]
    except:
        return None


def search_google(req):
    q = safe_get(req.args, 'q');
    if not q:
        return None
    s = requests.get(google_search_api + q)
    if s.ok:
        try:
            rst = json.loads(s.content)['responseData']['results']
        except:
            return None
        if isinstance(rst, list) and len(rst):
            return rst
        else:
            return None
    else:
        return None


if __name__ == '__main__':
    app.run()
