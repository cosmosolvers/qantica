from werkzeug.utils import secure_filename
from flask import url_for, send_from_directory
import os


def extension(filename, sign):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in EXTENSIONS[sign]


def upload(file, path=None):
    if file and extension(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(path, filename))
        return url_for(send_from_directory(path, filename), name=filename)
    return None
