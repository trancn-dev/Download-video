"""
Base Downloader class - Interface cho các downloader khác
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
import os
from pathlib import Path

from .utils import logger, sanitize_filename, ensure_dir


class BaseDownloader(ABC):
    """Base class cho tất cả downloaders"""

    def __init__(self, platform: str):
        """
        Initialize downloader

        Args:
            platform: Tên nền tảng (twitter, telegram, youtube, etc.)
        """
        self.platform = platform
        self.logger = logger

    @abstractmethod
    def download(self, url: str, **kwargs) -> Dict:
        """
        Download video từ URL

        Args:
            url: URL của video
            **kwargs: Các options khác (quality, output_dir, etc.)

        Returns:
            Dict với keys:
                - success: bool
                - filename: str (nếu success)
                - filesize: str (nếu có)
                - error: str (nếu failed)
        """
        pass

    @abstractmethod
    def get_available_formats(self, url: str) -> List[Dict]:
        """
        Lấy danh sách các format có sẵn

        Args:
            url: URL của video

        Returns:
            List of dicts, mỗi dict chứa:
                - format_id: str
                - height: int
                - fps: int
                - filesize: int (optional)
                - ext: str
        """
        pass

    def _prepare_output_path(self, output_dir: str, filename: str) -> Path:
        """
        Chuẩn bị đường dẫn output

        Args:
            output_dir: Thư mục output
            filename: Tên file

        Returns:
            Path object
        """
        # Ensure directory exists
        ensure_dir(output_dir)

        # Sanitize filename
        clean_filename = sanitize_filename(filename)

        # Create full path
        output_path = Path(output_dir) / clean_filename

        # Handle duplicate filenames
        counter = 1
        original_path = output_path
        while output_path.exists():
            stem = original_path.stem
            suffix = original_path.suffix
            output_path = original_path.parent / f"{stem}_{counter}{suffix}"
            counter += 1

        return output_path

    def _get_video_info(self, url: str) -> Dict:
        """
        Lấy thông tin video (title, duration, etc.)
        Override nếu cần

        Args:
            url: URL của video

        Returns:
            Dict chứa info
        """
        return {}
