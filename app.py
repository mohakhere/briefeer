from flask import Flask, render_template, request, redirect, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)

# Configure the upload folder
videos = UploadSet('videos', extensions=('mp4', 'avi', 'mkv'))
app.config['UPLOADED_VIDEOS_DEST'] = 'uploads'
configure_uploads(app, videos)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'video' in request.files:
        video = request.files['video']
        video_path = f"uploads/{video.filename}"
        video.save(video_path)
        return redirect(url_for('index'))
    return 'Error uploading video'

if __name__ == '__main__':
    app.run(debug=True)
