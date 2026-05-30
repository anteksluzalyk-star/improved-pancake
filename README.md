# 📦 File Share

A simple and elegant web application for uploading and downloading ZIP files. Perfect for sharing files with others without needing complex setup!

## Features

✨ **Easy Upload** - Drag and drop or click to upload ZIP files
📥 **Quick Download** - Anyone can download the shared file
🎨 **Modern UI** - Beautiful, responsive interface
⚡ **Fast** - Built with Flask for optimal performance
🔒 **File Management** - Only one file stored at a time (auto-replaces)
📊 **File Info** - View filename and file size

## Requirements

- Python 3.7+
- Flask
- Werkzeug

## Installation

1. Clone the repository:
```bash
git clone https://github.com/anteksluzalyk-star/improved-pancake.git
cd improved-pancake
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. **To upload**: Drag and drop a ZIP file or click to browse
4. **To download**: Click the download button (appears when a file is uploaded)

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main page with upload/download interface |
| `/upload` | POST | Upload a ZIP file |
| `/download` | GET | Download the uploaded file |
| `/status` | GET | Check if a file is available and get its info |

## Configuration

You can modify these settings in `app.py`:

- `MAX_FILE_SIZE` - Maximum file size (default: 100MB)
- `UPLOAD_FOLDER` - Directory to store uploads (default: `uploads/`)
- `ALLOWED_EXTENSIONS` - File types allowed (default: `{zip}`)

## File Storage

Uploaded files are stored in the `uploads/` directory. When a new file is uploaded, the previous one is automatically deleted (only one file at a time).

## Deployment

For production deployment:

1. Use a production WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

2. Set `debug=False` in `app.py`

3. Consider using HTTPS/SSL certificates

## License

MIT License - feel free to use and modify!

## Author

Created by anteksluzalyk-star
