from flask import Flask, jsonify, request
from typing import ByteString

app = Flask(__name__)


@app.route('/')
def index():
    return "Pravega Predictor welcomes you"


@app.route('/hello/<name>')
def say_hello(name: str):
    return jsonify({"developer": name})

# curl -X POST \
#   http://localhost:5000/capitalize-post \
#   -H 'Content-Type: application/json' \
#   -H 'Host: localhost:5000' \
#   -d '{"name": "shibasis"}'
@app.route('/capitalize-post', methods=['POST'])
def sample_post():
    data = request.get_json()
    name: str = data['name'] or ""
    return jsonify({'uppercaseName': name.upper()})


@app.route('/capitalize-get')
def query():
    name: str = request.args['name'] or ""
    return jsonify({'uppercaseName': name.upper()})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
