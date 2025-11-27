"""
Utility functions cho Video Downloader
"""

import os
import re
from pathlib import Path
from typing import Optional, Dict, List
from urllib.parse import urlparse
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def detect_platform(url: str) -> str:
    """
    Phát hiện nền tảng từ URL
    
    Args:
        url: URL của video
        
    Returns:
        Tên nền tảng: 'twitter', 'telegram', 'youtube', 'generic'
    """
    url_lower = url.lower()
    
    if 'twitter.com' in url_lower or 'x.com' in url_lower:
        return 'twitter'
    elif 't.me' in url_lower or 'telegram' in url_lower:
        return 'telegram'
    elif 'youtube.com' in url_lower or 'youtu.be' in url_lower:
        return 'youtube'
    elif 'facebook.com' in url_lower or 'fb.watch' in url_lower:
        return 'facebook'
    elif 'instagram.com' in url_lower:
        return 'instagram'
    elif 'tiktok.com' in url_lower:
        return 'tiktok'
    else:
        return 'generic'


def sanitize_filename(filename: str) -> str:
    """
    Làm sạch tên file, loại bỏ ký tự không hợp lệ
    
    Args:
        filename: Tên file gốc
        
    Returns:
        Tên file đã được làm sạch
    """
    # Loại bỏ ký tự đặc biệt
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Giới hạn độ dài
    if len(filename) > 200:
        name, ext = os.path.splitext(filename)
        filename = name[:200-len(ext)] + ext
    return filename


def ensure_dir(directory: str) -> Path:
    """
    Đảm bảo thư mục tồn tại, tạo mới nếu chưa có
    
    Args:
        directory: Đường dẫn thư mục
        
    Returns:
        Path object của thư mục
    """
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    return path


def format_bytes(bytes_size: int) -> str:
    """
    Format kích thước file sang dạng human-readable
    
    Args:
        bytes_size: Kích thước tính bằng bytes
        
    Returns:
        String dạng "10.5 MB"
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} PB"


def format_duration(seconds: int) -> str:
    """
    Format thời lượng video
    
    Args:
        seconds: Thời lượng tính bằng giây
        
    Returns:
        String dạng "1:23:45" hoặc "12:34"
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"


def parse_quality_string(quality: str) -> Dict:
    """
    Parse string chất lượng thành dict
    
    Args:
        quality: String như "1080p" hoặc "720p60"
        
    Returns:
        Dict với keys: height, fps
    """
    match = re.match(r'(\d+)p(\d+)?', quality)
    if match:
        height = int(match.group(1))
        fps = int(match.group(2)) if match.group(2) else 30
        return {'height': height, 'fps': fps}
    return {'height': 0, 'fps': 30}


def get_output_path(url: str, base_path: str, platform: Optional[str] = None) -> Path:
    """
    Tạo đường dẫn output cho video
    
    Args:
        url: URL của video
        base_path: Thư mục gốc
        platform: Nền tảng (optional, sẽ tự detect nếu None)
        
    Returns:
        Path object cho file output
    """
    if platform is None:
        platform = detect_platform(url)
    
    # Tạo thư mục con theo platform
    platform_dir = ensure_dir(os.path.join(base_path, platform))
    
    return platform_dir


def convert_wsl_path_to_windows(wsl_path: str) -> str:
    """
    Convert WSL path sang Windows path
    
    Args:
        wsl_path: Đường dẫn WSL (VD: /mnt/c/Users/...)
        
    Returns:
        Đường dẫn Windows (VD: C:\Users\...)
    """
    if wsl_path.startswith('/mnt/'):
        # /mnt/c/... -> C:/...
        parts = wsl_path.split('/')
        drive = parts[2].upper()
        rest = '/'.join(parts[3:])
        return f"{drive}:/{rest}".replace('/', '\\')
    return wsl_path


def convert_windows_path_to_wsl(windows_path: str) -> str:
    """
    Convert Windows path sang WSL path
    
    Args:
        windows_path: Đường dẫn Windows (VD: C:\Users\...)
        
    Returns:
        Đường dẫn WSL (VD: /mnt/c/Users/...)
    """
    if ':' in windows_path:
        # C:\... -> /mnt/c/... 
        drive = windows_path[0].lower()
        rest = windows_path[3:].replace('\\', '/')
        return f"/mnt/{drive}/{rest}"
    return windows_path


def is_valid_url(url: str) -> bool:
    """
    Kiểm tra URL có hợp lệ không
    
    Args:
        url: URL cần kiểm tra
        
    Returns:
        True nếu hợp lệ, False nếu không
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def select_best_format(formats: List[Dict], prefer_quality: str = 'best') -> Dict:
    """
    Chọn format tốt nhất từ danh sách
    
    Args:
        formats: List các format có sẵn
        prefer_quality: 'best', 'worst', hoặc resolution cụ thể như '1080p'
        
    Returns:
        Format được chọn
    """
    if not formats:
        return None
    
    if prefer_quality == 'worst':
        return min(formats, key=lambda f: f.get('height', 0))
    elif prefer_quality == 'best':
        return max(formats, key=lambda f: f.get('height', 0))
    else:
        # Tìm format gần nhất với quality yêu cầu
        target_height = parse_quality_string(prefer_quality)['height']
        return min(formats, key=lambda f: abs(f.get('height', 0) - target_height))


class ProgressBar:
    """Class đơn giản để hiển thị progress"""
    
    def __init__(self, total: int, description: str = "Downloading"):
        self.total = total
        self.current = 0
        self.description = description
    
    def update(self, amount: int = 1):
        """Cập nhật progress"""
        self.current += amount
        percentage = (self.current / self.total) * 100 if self.total > 0 else 0
        bar_length = 40
        filled = int(bar_length * self.current / self.total) if self.total > 0 else 0
        bar = '█' * filled + '-' * (bar_length - filled)
        print(f'\r{self.description}: |{bar}| {percentage:.1f}%', end='', flush=True)
        
        if self.current >= self.total:
            print()  # New line khi hoàn thành