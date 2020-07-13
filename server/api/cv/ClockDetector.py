from flask import Blueprint, request
import os
import random
from werkzeug.utils import secure_filename

from server.models.clock.getTime import detectTimeFrom

clock_detector = Blueprint('clock_detector', __name__)


@clock_detector.route('/upload-clock', methods=["POST"])
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
        return time
