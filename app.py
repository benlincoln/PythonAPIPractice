import json

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<name>', methods=['GET'])
def hello_name(name):
    return 'Hello ' + name + '!'


@app.route('/json', methods=['GET'])
def json_return():
    return json.dumps({'return': 'fish'})


if __name__ == '__main__':
    app.run()
