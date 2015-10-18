from flask import Flask
from routes.index import index
from routes.search import search

def main():
    app = Flask(__name__)
    app.register_blueprint(index)
    app.register_blueprint(search)
    app.run(port=5080)

if __name__ == '__main__':
    main()
