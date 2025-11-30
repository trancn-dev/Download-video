#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Start web server
echo "🚀 Starting Video Downloader Web UI..."
echo "📱 Web interface will be available at:"
echo "   - http://localhost:5000"
echo "   - http://127.0.0.1:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python web_app.py
