from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "Pravega Predictor welcomes you"


@app.route('/hello/<name>')
def say_hello(name):
    return jsonify({"developer": name})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
