"""
Downloader Factory
Trả về downloader phù hợp cho mỗi platform
"""

from .base_downloader import BaseDownloader
from .generic_downloader import GenericDownloader
from .twitter_downloader import TwitterDownloader
from .telegram_downloader import TelegramDownloader
from .utils import logger


def get_downloader(platform: str) -> BaseDownloader:
    """
    Get appropriate downloader cho platform

    Args:
        platform: Tên platform (twitter, telegram, youtube, generic, etc.)

    Returns:
        Instance của downloader

    Raises:
        ValueError: Nếu platform không được hỗ trợ
    """
    platform = platform.lower()

    if platform in ['twitter', 'x']:
        logger.info("Using Twitter downloader")
        return TwitterDownloader()

    elif platform == 'telegram':
        logger.info("Using Telegram downloader")
        try:
            return TelegramDownloader()
        except (ImportError, ValueError) as e:
            logger.warning(f"Telegram downloader not available: {e}")
            logger.info("Falling back to generic downloader")
            return GenericDownloader(platform)

    elif platform in ['youtube', 'facebook', 'instagram', 'tiktok', 'reddit', 'twitch']:
        logger.info(f"Using generic downloader for {platform}")
        return GenericDownloader(platform)

    else:
        logger.info("Using generic downloader")
        return GenericDownloader(platform)
