from flask import Flask, jsonify, request, render_template, redirect
import os
import random
from werkzeug.utils import secure_filename

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

# Learn at -> https://pythonise.com/series/learning-flask/flask-uploading-files
@app.route('/upload-clock', methods=["GET", "POST"])
def upload_clock():
    if request.method == "GET":
        return render_template("uploadImage.html")

    if request.method == "POST" and request.files:
        image = request.files['clock_image']
        filename = secure_filename(f'clock_image_{random.randint(3791, 48921)}.jpg')
        image.save(os.path.join('./temp', filename))
        print(f" Saving {image} as {filename}")
        return redirect(request.url)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
