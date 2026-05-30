from flask import Flask, render_template, request, send_file, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'zip'}
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if file is present
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Only ZIP files are allowed'}), 400
    
    try:
        # Remove old file if exists
        for f in os.listdir(UPLOAD_FOLDER):
            os.remove(os.path.join(UPLOAD_FOLDER, f))
        
        filename = secure_filename('shared_file.zip')
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        return jsonify({
            'success': True,
            'message': 'File uploaded successfully',
            'filename': filename
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/download')
def download_file():
    try:
        files = os.listdir(UPLOAD_FOLDER)
        if not files:
            return jsonify({'error': 'No file available for download'}), 404
        
        filepath = os.path.join(UPLOAD_FOLDER, files[0])
        return send_file(filepath, as_attachment=True, download_name='shared_file.zip')
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/status')
def status():
    try:
        files = os.listdir(UPLOAD_FOLDER)
        if files:
            filepath = os.path.join(UPLOAD_FOLDER, files[0])
            file_size = os.path.getsize(filepath)
            return jsonify({
                'has_file': True,
                'filename': files[0],
                'size': file_size,
                'size_mb': round(file_size / (1024 * 1024), 2)
            })
        return jsonify({'has_file': False})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
