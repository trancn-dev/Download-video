"""
Generic Downloader sử dụng yt-dlp
Hỗ trợ 1000+ websites
"""

import yt_dlp
from typing import Dict, List, Optional
from pathlib import Path

from .base_downloader import BaseDownloader
from .config import (
    YTDLP_BASE_OPTIONS,
    FFMPEG_PATH,
    DEFAULT_USER_AGENT,
    QUALITY_PRESETS
)
from .utils import format_bytes, logger


class GenericDownloader(BaseDownloader):
    """Downloader sử dụng yt-dlp cho hầu hết các platform"""

    def __init__(self, platform: str = 'generic'):
        super().__init__(platform)
        self.ydl_opts = YTDLP_BASE_OPTIONS.copy()

    def get_available_formats(self, url: str) -> List[Dict]:
        """Lấy danh sách formats có sẵn"""
        try:
            with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                info = ydl.extract_info(url, download=False)

                if 'formats' not in info:
                    return []

                formats = []
                for fmt in info['formats']:
                    formats.append({
                        'format_id': fmt.get('format_id'),
                        'ext': fmt.get('ext'),
                        'height': fmt.get('height', 0),
                        'width': fmt.get('width', 0),
                        'fps': fmt.get('fps', 30),
                        'filesize': fmt.get('filesize', 0),
                        'vcodec': fmt.get('vcodec', 'none'),
                        'acodec': fmt.get('acodec', 'none'),
                        'format_note': fmt.get('format_note', '')
                    })

                return formats

        except Exception as e:
            logger.error(f"Error getting formats: {e}")
            return []

    def download(self, url: str, **kwargs) -> Dict:
        """
        Download video

        Args:
            url: URL của video
            **kwargs:
                - output_dir: Thư mục output (default: ./downloads)
                - format_id: ID của format cụ thể
                - preset: Preset chất lượng (best, high, medium, low)
                - audio_only: True để chỉ tải audio
                - merge: True để merge video+audio (default: True)
                - verbose: True để hiện log chi tiết

        Returns:
            Dict với success, filename, filesize, error
        """
        output_dir = kwargs.get('output_dir', './downloads')
        format_id = kwargs.get('format_id')
        preset = kwargs.get('preset', 'best')
        audio_only = kwargs.get('audio_only', False)
        merge = kwargs.get('merge', True)
        verbose = kwargs.get('verbose', False)

        # Build yt-dlp options
        ydl_opts = self.ydl_opts.copy()

        # Tạo thư mục con theo platform
        platform_dir = Path(output_dir) / self.platform
        platform_dir.mkdir(parents=True, exist_ok=True)

        ydl_opts['outtmpl'] = str(platform_dir / '%(title)s.%(ext)s')
        ydl_opts['quiet'] = not verbose

        # Format selection
        if audio_only:
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        elif format_id:
            ydl_opts['format'] = format_id
        elif preset in QUALITY_PRESETS:
            ydl_opts['format'] = QUALITY_PRESETS[preset]

        # Merge options
        if not merge:
            ydl_opts['postprocessors'] = []

        # Progress hook
        downloaded_file = {'path': None, 'size': None}

        def progress_hook(d):
            if d['status'] == 'downloading':
                total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
                downloaded = d.get('downloaded_bytes', 0)
                speed = d.get('speed', 0)
                eta = d.get('eta', 0)

                if total > 0:
                    percent = (downloaded / total) * 100
                    speed_str = format_bytes(speed) + '/s' if speed else 'N/A'
                    print(f"\r⬇️  {percent:.1f}% - {format_bytes(downloaded)}/{format_bytes(total)} @ {speed_str}", end='', flush=True)

            elif d['status'] == 'finished':
                print(f"\n✅ Download hoàn thành, đang xử lý...")
                downloaded_file['path'] = d.get('filename')
                downloaded_file['size'] = d.get('total_bytes', 0)

        ydl_opts['progress_hooks'] = [progress_hook]

        # Download
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)

                # Get final filename
                if downloaded_file['path']:
                    final_path = downloaded_file['path']
                else:
                    final_path = ydl.prepare_filename(info)

                # Get filesize
                filesize = downloaded_file['size']
                if not filesize and Path(final_path).exists():
                    filesize = Path(final_path).stat().st_size

                return {
                    'success': True,
                    'filename': final_path,
                    'filesize': format_bytes(filesize) if filesize else 'Unknown',
                    'title': info.get('title', 'Unknown'),
                    'duration': info.get('duration', 0)
                }

        except yt_dlp.utils.DownloadError as e:
            logger.error(f"Download error: {e}")
            return {
                'success': False,
                'error': str(e)
            }

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return {
                'success': False,
                'error': str(e)
            }
