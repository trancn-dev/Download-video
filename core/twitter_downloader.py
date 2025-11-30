"""
Twitter/X Downloader
Hỗ trợ download video từ Twitter/X, bao gồm protected tweets
"""

from .generic_downloader import GenericDownloader
from .config import TWITTER_AUTH_TOKEN, COOKIES_FILE
from .utils import logger
import os


class TwitterDownloader(GenericDownloader):
    """Downloader cho Twitter/X"""

    def __init__(self):
        super().__init__(platform='twitter')

        # Add Twitter-specific options
        self.ydl_opts['cookiefile'] = str(COOKIES_FILE) if COOKIES_FILE.exists() else None

        # Nếu có auth token, có thể thêm vào headers
        if TWITTER_AUTH_TOKEN:
            self.ydl_opts['http_headers'] = {
                'Authorization': f'Bearer {TWITTER_AUTH_TOKEN}'
            }

    def download(self, url: str, **kwargs) -> dict:
        """
        Download video từ Twitter/X

        Hỗ trợ:
        - Public tweets
        - Protected tweets (cần cookies hoặc auth token)
        - Video threads
        """
        # Normalize URL
        url = url.replace('twitter.com', 'x.com')

        logger.info(f"Downloading from Twitter: {url}")

        # Check authentication
        if not COOKIES_FILE.exists() and not TWITTER_AUTH_TOKEN:
            logger.warning("No Twitter authentication configured. May fail for protected content.")
            logger.warning("See TWITTER_AUTH.md for setup instructions.")

        return super().download(url, **kwargs)
