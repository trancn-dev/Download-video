"""
Configuration và constants cho Video Downloader
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===== PATHS =====
BASE_DIR = Path(__file__).parent.parent
DEFAULT_DOWNLOAD_DIR = os.getenv('DOWNLOAD_DIR', str(BASE_DIR / 'downloads'))
TEMP_DIR = BASE_DIR / 'temp'
COOKIES_FILE = BASE_DIR / 'cookies.txt'

# ===== TELEGRAM CONFIG =====
TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')
TELEGRAM_PHONE = os.getenv('TELEGRAM_PHONE')
TELEGRAM_SESSION_NAME = os.getenv('TELEGRAM_SESSION_NAME', 'video_downloader')

# ===== TWITTER/X CONFIG =====
TWITTER_AUTH_TOKEN = os.getenv('TWITTER_AUTH_TOKEN')
TWITTER_CSRF_TOKEN = os.getenv('TWITTER_CSRF_TOKEN')

# ===== DOWNLOAD OPTIONS =====
DEFAULT_QUALITY = os.getenv('DEFAULT_QUALITY', 'best')
MAX_CONCURRENT_DOWNLOADS = int(os.getenv('MAX_CONCURRENT_DOWNLOADS', '3'))
CHUNK_SIZE = 1024 * 1024  # 1MB chunks
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

# ===== QUALITY PRESETS =====
QUALITY_PRESETS = {
    'best': 'bestvideo+bestaudio/best',
    'high': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    'medium': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
    'low': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
}

# ===== YT-DLP OPTIONS =====
YTDLP_BASE_OPTIONS = {
    'quiet': False,
    'no_warnings': False,
    'extract_flat': False,
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
    'outtmpl': '%(title)s.%(ext)s',
    'progress_hooks': [],
}

# ===== FFMPEG CONFIG =====
FFMPEG_PATH = os.getenv('FFMPEG_PATH', 'ffmpeg')
FFPROBE_PATH = os.getenv('FFPROBE_PATH', 'ffprobe')

# ===== WEB APP CONFIG =====
WEB_HOST = os.getenv('WEB_HOST', '0.0.0.0')
WEB_PORT = int(os.getenv('WEB_PORT', '5000'))
WEB_DEBUG = os.getenv('WEB_DEBUG', 'False').lower() == 'true'

# ===== LOGGING =====
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = BASE_DIR / 'downloader.log'

# ===== USER AGENTS =====
USER_AGENTS = {
    'chrome': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'firefox': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'mobile': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
}

DEFAULT_USER_AGENT = USER_AGENTS['chrome']

# ===== PLATFORM-SPECIFIC =====
TWITTER_GRAPHQL_ENDPOINTS = {
    'tweet_detail': 'https://twitter.com/i/api/graphql/5GOHgZe-8U2j5sVHQzEm9A/TweetDetail',
}

TELEGRAM_MEDIA_TYPES = ['photo', 'video', 'animation', 'document']

# ===== SUPPORTED PLATFORMS =====
SUPPORTED_PLATFORMS = [
    'twitter', 'x', 'telegram', 'youtube', 'facebook',
    'instagram', 'tiktok', 'reddit', 'twitch', 'generic'
]

# ===== FILE EXTENSIONS =====
VIDEO_EXTENSIONS = ['.mp4', '.mkv', '.webm', '.avi', '.mov', '.flv', '.wmv']
AUDIO_EXTENSIONS = ['.mp3', '.m4a', '.opus', '.ogg', '.wav', '.flac']

# ===== VALIDATION =====
def validate_config():
    """Validate configuration"""
    errors = []

    # Check Telegram config if needed
    if not all([TELEGRAM_API_ID, TELEGRAM_API_HASH]):
        errors.append("⚠️  Telegram credentials not configured (optional)")

    # Check Twitter config if needed
    if not TWITTER_AUTH_TOKEN:
        errors.append("⚠️  Twitter credentials not configured (optional)")

    # Check FFmpeg
    import shutil
    if not shutil.which(FFMPEG_PATH):
        errors.append("❌ FFmpeg not found! Please install: sudo apt install ffmpeg")

    return errors


# Validate on import
_validation_errors = validate_config()
if _validation_errors:
    import logging
    logger = logging.getLogger(__name__)
    for error in _validation_errors:
        logger.warning(error)
