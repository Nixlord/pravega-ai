from flask import Blueprint, request

samples = Blueprint('samples', __name__)


@samples.route('/hello/<name>')
def say_hello(name: str):
    return {"developer": name}


# curl -X POST \
#   http://localhost:5000/capitalize-post \
#   -H 'Content-Type: application/json' \
#   -H 'Host: localhost:5000' \
#   -d '{"name": "shibasis"}'
@samples.route('/capitalize-post', methods=['POST'])
def sample_post():
    data = request.get_json()
    name: str = data['name'] or ""
    return {'uppercaseName': name.upper()}


@samples.route('/capitalize-get ')
def query():
    name: str = request.args['name'] or ""
    return {'uppercaseName': name.upper()}
