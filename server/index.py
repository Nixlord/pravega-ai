from flask import Flask, request, render_template

from server.api.cv.ClockDetector import clock_detector
from server.api.samples.Sample import samples

print(__name__)
print(__package__)

app = Flask(__name__)
# app = Flask(__name__, template_folder='./build', static_folder='./build/static', static_url_path='/')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_react(path):
    return render_template("index.html")


# Learn at -> https://pythonise.com/series/learning-flask/flask-uploading-files
@app.route('/upload-clock', methods=["GET"])
def upload_clock_view():
    return render_template("uploadImage.html")


app.register_blueprint(clock_detector, url_prefix='/api')
app.register_blueprint(samples, url_prefix='/sample-api')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
