"""
Core package for Video Downloader
"""

from .utils import (
    detect_platform,
    sanitize_filename,
    ensure_dir,
    format_bytes,
    format_duration,
    is_valid_url,
    logger
)

from .config import (
    DEFAULT_DOWNLOAD_DIR,
    QUALITY_PRESETS,
    SUPPORTED_PLATFORMS
)

__version__ = '1.0.0'
__all__ = [
    'detect_platform',
    'sanitize_filename',
    'ensure_dir',
    'format_bytes',
    'format_duration',
    'is_valid_url',
    'logger',
    'DEFAULT_DOWNLOAD_DIR',
    'QUALITY_PRESETS',
    'SUPPORTED_PLATFORMS'
]
