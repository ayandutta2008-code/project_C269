import os
import cv2
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_image():
    width = int(request.form['width'])
    height = int(request.form['height'])
    image_file = request.files['file']
    filename = secure_filename(image_file.filename)
    reading_file_data = image_file.read()
    image_file.save(os.path.join('static/', filename))
    image =  Image.open(image_file)
    image.thumbnail((width, height))
    mage_file.save(os.path.join('static/', filename))
    image_array = np.fromstring(reading_file_data, dtype='uint8')
    decode_array_to_img = cv2.imdecode(image_array, cv2.IMREAD_UNCHANGED)
    return render_template('upload.html', filename=filename)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))


if __name__ == "__main__":
    app.run()
