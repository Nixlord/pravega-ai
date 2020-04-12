from flask import Flask, jsonify, request, render_template, redirect
import os
import random
from werkzeug.utils import secure_filename

from src.models.clock.getTime import detectTimeFrom

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
@app.route('/upload-clock', methods=["GET"])
def upload_clock_view():
    return render_template("uploadImage.html")


@app.route('/api/upload-clock', methods=["POST"])
def upload_clock():
    if request.files:
        image = request.files['clock_image']
        # Of course a much better mechanism is required. This is PoC
        filename = secure_filename(f'clock_image_{random.randint(1000, 9999)}.jpg')

        if not os.path.exists('./temp'):
            os.makedirs('./temp')

        image_path = os.path.join('./temp', filename)
        image.save(image_path)
        print(f" Saving {image} as {image_path}")
        time = detectTimeFrom(image_path)
        print(f"Time: {time}")
        return jsonify(time)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
