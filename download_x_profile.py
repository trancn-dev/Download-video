#!/usr/bin/env python3
"""
Download tất cả images và videos từ X/Twitter profile
Tạo thư mục riêng cho mỗi user: downloads/twitter/username/

Usage:
    python download_x_profile.py https://x.com/username
    python download_x_profile.py https://twitter.com/username
"""

import sys
import re
from pathlib import Path
import subprocess
import json
from typing import Optional, Dict, List

from core.config import TWITTER_AUTH_TOKEN, COOKIES_FILE, DEFAULT_DOWNLOAD_DIR
from core.utils import logger


class XProfileDownloader:
    """Download tất cả media từ X/Twitter profile"""

    def __init__(self, profile_url: str):
        self.profile_url = profile_url
        self.username = self._extract_username(profile_url)

        if not self.username:
            raise ValueError(f"Invalid X/Twitter profile URL: {profile_url}")

        # Tạo thư mục: downloads/x/username/
        self.output_dir = Path(DEFAULT_DOWNLOAD_DIR) / 'x' / self.username
        self.output_dir.mkdir(parents=True, exist_ok=True)

        logger.info(f"📂 Output directory: {self.output_dir}")

    def _extract_username(self, url: str) -> Optional[str]:
        """Extract username từ URL"""
        # https://x.com/username hoặc https://twitter.com/username
        patterns = [
            r'(?:x\.com|twitter\.com)/([a-zA-Z0-9_]+)',
            r'^@?([a-zA-Z0-9_]+)$'  # Direct username
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None

    def _build_gallery_dl_command(self) -> List[str]:
        """Build gallery-dl command để download tất cả media"""
        cmd = [
            'gallery-dl',
            f'https://x.com/{self.username}',  # Profile URL
            '--dest', str(self.output_dir),  # Thư mục đích
            '--directory', '',  # Không tạo subfolder
            '--filename', '{tweet_id}_{num}.{extension}',  # Format: tweetid_1.jpg
        ]

        # Authentication
        if COOKIES_FILE.exists():
            cmd.extend(['--cookies', str(COOKIES_FILE)])
            logger.info(f"🍪 Using cookies from: {COOKIES_FILE}")
        elif TWITTER_AUTH_TOKEN:
            # Extract bearer token từ TWITTER_AUTH_TOKEN
            token = TWITTER_AUTH_TOKEN.replace('Bearer ', '').strip()
            cmd.extend([
                '--option', f'extractor.twitter.bearer-token={token}'
            ])
            logger.info("🔑 Using auth token from .env")
        else:
            logger.info("ℹ️  Downloading without authentication (public tweets only)")

        # Options
        cmd.extend([
            '--no-skip',  # Không skip files
            '--retries', '5',
            '--range', '1-9999',  # Download ALL tweets (mặc định chỉ tải vài cái gần nhất)
            '--option', 'retweets=true',  # Bao gồm cả retweets (bài đăng lại)
        ])

        return cmd

    def download_all(self) -> Dict:
        """Download tất cả media từ profile"""
        logger.info(f"🚀 Bắt đầu tải media từ @{self.username}")
        logger.info(f"📁 Lưu vào: {self.output_dir}")

        cmd = self._build_gallery_dl_command()

        # Log command (hide sensitive info)
        safe_cmd = [c if 'Bearer' not in c else '[AUTH_TOKEN]' for c in cmd]
        logger.debug(f"Command: {' '.join(safe_cmd)}")

        print(f"\n{'='*60}")
        print(f"📥 Downloading from: @{self.username}")
        print(f"📂 Output folder: {self.output_dir}")
        print(f"{'='*60}\n")

        try:
            # Run yt-dlp
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
            )

            # Stream output
            downloaded = 0
            errors = 0

            for line in process.stdout:
                line = line.strip()
                if line:
                    print(line)

                    # Count downloads
                    if '[download] Destination:' in line or 'has already been downloaded' in line:
                        downloaded += 1
                    elif 'ERROR' in line.upper():
                        errors += 1

            process.wait()
            exit_code = process.returncode

            # Summary
            print(f"\n{'='*60}")
            if exit_code == 0:
                print(f"✅ Hoàn thành!")
            else:
                print(f"⚠️  Hoàn thành với một số lỗi (exit code: {exit_code})")

            # Count files
            files = list(self.output_dir.glob('*'))
            media_files = [f for f in files if f.suffix in ['.jpg', '.png', '.mp4', '.webm', '.gif']]

            print(f"📊 Tổng files: {len(media_files)}")
            print(f"📁 Thư mục: {self.output_dir}")
            print(f"{'='*60}\n")

            return {
                'success': exit_code == 0,
                'username': self.username,
                'output_dir': str(self.output_dir),
                'total_files': len(media_files),
                'downloaded': downloaded,
                'errors': errors
            }

        except KeyboardInterrupt:
            print("\n\n❌ Đã hủy bởi user")
            return {
                'success': False,
                'error': 'Cancelled by user'
            }
        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"\n❌ Lỗi: {e}")
            return {
                'success': False,
                'error': str(e)
            }

    def list_files(self):
        """List tất cả files đã tải"""
        files = sorted(self.output_dir.glob('*'))

        if not files:
            print(f"📭 Chưa có file nào trong {self.output_dir}")
            return

        print(f"\n📁 Files trong {self.output_dir}:\n")

        images = [f for f in files if f.suffix in ['.jpg', '.png', '.gif', '.webp']]
        videos = [f for f in files if f.suffix in ['.mp4', '.webm', '.mov']]
        others = [f for f in files if f not in images and f not in videos]

        if images:
            print(f"🖼️  Images ({len(images)}):")
            for f in images[:10]:  # Show first 10
                size = f.stat().st_size / 1024 / 1024  # MB
                print(f"  - {f.name} ({size:.2f} MB)")
            if len(images) > 10:
                print(f"  ... and {len(images) - 10} more")

        if videos:
            print(f"\n🎥 Videos ({len(videos)}):")
            for f in videos[:10]:
                size = f.stat().st_size / 1024 / 1024  # MB
                print(f"  - {f.name} ({size:.2f} MB)")
            if len(videos) > 10:
                print(f"  ... and {len(videos) - 10} more")

        if others:
            print(f"\n📄 Other files ({len(others)}):")
            for f in others[:5]:
                print(f"  - {f.name}")


def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("""
🐦 X/Twitter Profile Media Downloader

Usage:
    python download_x_profile.py <profile_url>

Examples:
    python download_x_profile.py https://x.com/tkdong197
    python download_x_profile.py https://twitter.com/elonmusk
    python download_x_profile.py tkdong197

Options:
    --list    List downloaded files without downloading

Note:
    - Requires TWITTER_AUTH_TOKEN or cookies.txt (see TWITTER_AUTH.md)
    - Files will be saved to: downloads/twitter/username/
    - Automatically skips already downloaded files
        """)
        sys.exit(1)

    profile_url = sys.argv[1]

    # Check for --list flag
    list_only = '--list' in sys.argv

    try:
        downloader = XProfileDownloader(profile_url)

        if list_only:
            downloader.list_files()
        else:
            result = downloader.download_all()

            if result.get('success'):
                print(f"\n✅ Đã tải xong media từ @{result['username']}")
                print(f"📂 Xem files tại: {result['output_dir']}")
            else:
                print(f"\n❌ Download thất bại: {result.get('error', 'Unknown error')}")
                sys.exit(1)

    except ValueError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
