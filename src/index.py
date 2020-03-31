from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Pravega Predictor welcomes you"


@app.route('/hello/<name>')
def say_hello(name):
    return jsonify({"developer": name})


@app.route('query')
def query():
    if 'name' in request.args:
        return jsonify({'queryResults': request.args['name']})
    else:
        return jsonify({'queryResults': None})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
