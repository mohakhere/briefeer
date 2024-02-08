from flask import Flask, render_template, request, redirect, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
import logging
app = Flask(__name__)

videos = UploadSet('videos', extensions=('mp4', 'avi', 'mkv'))
app.config['UPLOADED_VIDEOS_DEST'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
logging.basicConfig(filename='app.log', level=logging.INFO)
videos = UploadSet('videos', extensions=('mp4', 'avi', 'mkv'))
configure_uploads(app, videos)
@app.route('/upload', methods=['POST'])
def upload():
    if 'video' in request.files:
        video = request.files['video']
        video_path = os.path.join('uploads', video.filename)
        if os.path.exists(video_path):
            logging.warning(f"File already exists: {video.filename}")
            return 'File with this name already exists'
        try:
            video.save(video_path)
            logging.info(f"Uploaded: {video.filename}")
            return redirect(url_for('index'))
        except Exception as e:
            logging.error(f"Error uploading {video.filename}: {str(e)}")
            return 'Error uploading video'
    return 'Error uploading video'
if __name__ == '__main__':
    app.run(debug=True)
