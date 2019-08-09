from flask import Flask, render_template, url_for, request, send_file
from werkzeug.utils import secure_filename
from scan import scan_image
import os

# UPLOAD_FOLDER = 'uploads'
UPLOADED_FILE = 'uploads/uploaded.png'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        imageFile = request.files['imageFile']
        imageFile.save(UPLOADED_FILE)
        scanned_image = scan_image(UPLOADED_FILE)
        scanned_image.save('scanned_images/scanned_image.png')

        return send_file('scanned_images/scanned_image.png')

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
