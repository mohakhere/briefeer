from flask import Flask, render_template, request, redirect, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

# Configure the upload folder
videos = UploadSet('videos', extensions=('mp4', 'avi', 'mkv'))
app.config['UPLOADED_VIDEOS_DEST'] = 'uploads'
configure_uploads(app, videos)
