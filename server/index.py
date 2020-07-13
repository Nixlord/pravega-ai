from flask import Flask, request, render_template

from server.api.cv.ClockDetector import clock_detector
from server.api.samples.Sample import samples

app = Flask(__name__, template_folder='./build', static_folder='./build/static', static_url_path='/')


# UI
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_react(path):
    return render_template("index.html")


# API Register
app.register_blueprint(clock_detector, url_prefix='/api')
app.register_blueprint(samples, url_prefix='/sample-api')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
