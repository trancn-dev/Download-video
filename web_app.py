#!/usr/bin/env python3
"""
Web App cho Video Downloader
Simple web interface để download video
"""

from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import os
from pathlib import Path
from threading import Thread
import uuid

from core.utils import detect_platform, is_valid_url, logger
from core.config import WEB_HOST, WEB_PORT, WEB_DEBUG, DEFAULT_DOWNLOAD_DIR
from core.downloader_factory import get_downloader

app = Flask(__name__)
CORS(app)

# Store download status
downloads = {}


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/api/detect', methods=['POST'])
def detect():
    """Detect platform từ URL"""
    data = request.get_json()
    url = data.get('url', '')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    if not is_valid_url(url):
        return jsonify({'error': 'Invalid URL'}), 400

    platform = detect_platform(url)

    return jsonify({
        'platform': platform,
        'url': url
    })


@app.route('/api/formats', methods=['POST'])
def get_formats():
    """Lấy danh sách formats có sẵn"""
    data = request.get_json()
    url = data.get('url', '')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        platform = detect_platform(url)
        downloader = get_downloader(platform)
        formats = downloader.get_available_formats(url)

        return jsonify({
            'success': True,
            'formats': formats
        })

    except Exception as e:
        logger.error(f"Error getting formats: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/download', methods=['POST'])
def download():
    """Start download"""
    data = request.get_json()
    url = data.get('url', '')
    quality = data.get('quality', 'best')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Generate download ID
    download_id = str(uuid.uuid4())

    # Initialize download status
    downloads[download_id] = {
        'status': 'pending',
        'progress': 0,
        'filename': None,
        'error': None
    }

    # Start download in background thread
    thread = Thread(target=perform_download, args=(download_id, url, quality))
    thread.daemon = True
    thread.start()

    return jsonify({
        'success': True,
        'download_id': download_id
    })


def perform_download(download_id: str, url: str, quality: str):
    """Perform download in background"""
    try:
        downloads[download_id]['status'] = 'downloading'

        platform = detect_platform(url)
        downloader = get_downloader(platform)

        # Download
        result = downloader.download(
            url,
            output_dir=DEFAULT_DOWNLOAD_DIR,
            preset=quality
        )

        if result['success']:
            downloads[download_id]['status'] = 'completed'
            downloads[download_id]['filename'] = result['filename']
            downloads[download_id]['filesize'] = result.get('filesize', 'Unknown')
        else:
            downloads[download_id]['status'] = 'failed'
            downloads[download_id]['error'] = result.get('error', 'Unknown error')

    except Exception as e:
        logger.error(f"Download error: {e}")
        downloads[download_id]['status'] = 'failed'
        downloads[download_id]['error'] = str(e)


@app.route('/api/status/<download_id>')
def get_status(download_id):
    """Lấy status của download"""
    if download_id not in downloads:
        return jsonify({'error': 'Download not found'}), 404

    return jsonify(downloads[download_id])


@app.route('/api/download/<download_id>/file')
def download_file(download_id):
    """Download file đã tải về"""
    if download_id not in downloads:
        return jsonify({'error': 'Download not found'}), 404

    download_info = downloads[download_id]

    if download_info['status'] != 'completed':
        return jsonify({'error': 'Download not completed'}), 400

    filepath = download_info['filename']

    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404

    return send_file(filepath, as_attachment=True)


@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    # Ensure download directory exists
    Path(DEFAULT_DOWNLOAD_DIR).mkdir(parents=True, exist_ok=True)

    print(f"""
    🎥 Video Downloader Web App

    🌐 Server running at: http://{WEB_HOST}:{WEB_PORT}
    📁 Downloads will be saved to: {DEFAULT_DOWNLOAD_DIR}

    Press Ctrl+C to stop
    """)

    app.run(
        host=WEB_HOST,
        port=WEB_PORT,
        debug=WEB_DEBUG
    )
