"""
Telegram Downloader
Hỗ trợ download video từ Telegram channels, groups (bao gồm private)
"""

from typing import Dict, List, Optional
from pathlib import Path
import asyncio

from .base_downloader import BaseDownloader
from .config import (
    TELEGRAM_API_ID,
    TELEGRAM_API_HASH,
    TELEGRAM_PHONE,
    TELEGRAM_SESSION_NAME
)
from .utils import logger, format_bytes

# Lazy import Telethon để không bắt buộc phải cài
try:
    from telethon import TelegramClient
    from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False
    logger.warning("Telethon not installed. Telegram downloads will not work.")


class TelegramDownloader(BaseDownloader):
    """Downloader cho Telegram"""

    def __init__(self):
        super().__init__(platform='telegram')

        if not TELETHON_AVAILABLE:
            raise ImportError("Telethon is required for Telegram downloads. Install with: pip install telethon")

        if not all([TELEGRAM_API_ID, TELEGRAM_API_HASH]):
            raise ValueError("Telegram API credentials not configured. See TELEGRAM_SETUP.md")

        self.client = None

    async def _init_client(self):
        """Initialize Telegram client"""
        if self.client is None:
            self.client = TelegramClient(
                TELEGRAM_SESSION_NAME,
                int(TELEGRAM_API_ID),
                TELEGRAM_API_HASH
            )

            # Connect first
            await self.client.connect()

            # Then authorize if needed
            if not await self.client.is_user_authorized():
                try:
                    await self.client.start(
                        phone=TELEGRAM_PHONE,
                        code_callback=lambda: input('Please enter the code you received: '),
                        password=lambda: input('Please enter your password (or press Enter if no 2FA): ') or None
                    )
                except Exception as e:
                    logger.error(f"Failed to authorize: {e}")
                    raise

            logger.info("Telegram client initialized")

    async def _download_video(self, url: str, output_dir: str) -> Dict:
        """Download video từ Telegram"""
        try:
            await self._init_client()

            # Parse URL để lấy message
            # Format: https://t.me/channel_name/message_id hoặc https://t.me/c/channel_id/message_id
            parts = url.rstrip('/').split('/')
            if len(parts) < 2:
                return {'success': False, 'error': 'Invalid Telegram URL'}

            # Check if private channel (format: /c/1234567890/123)
            if len(parts) >= 3 and parts[-3] == 'c':
                # Private channel - convert to -100 format
                channel_id = int(parts[-2])
                channel_name = -1000000000000 - channel_id  # Convert to supergroup ID
                message_id = int(parts[-1])
                logger.info(f"Fetching message {message_id} from private channel {channel_id}")
            else:
                # Public channel (format: /channel_name/123)
                channel_name = parts[-2]
                message_id = int(parts[-1])
                logger.info(f"Fetching message {message_id} from {channel_name}")

            # Get message
            message = await self.client.get_messages(channel_name, ids=message_id)

            if not message:
                return {'success': False, 'error': 'Message not found'}

            # Check if message has media
            if not message.media:
                return {'success': False, 'error': 'No media in message'}

            # Download media
            if isinstance(message.media, (MessageMediaPhoto, MessageMediaDocument)):
                # Tạo thư mục riêng cho Telegram
                output_path = Path(output_dir) / 'telegram'
                output_path.mkdir(parents=True, exist_ok=True)

                # Progress callback
                def progress_callback(current, total):
                    percent = (current / total) * 100
                    print(f"\r⬇️  {percent:.1f}% - {format_bytes(current)}/{format_bytes(total)}", end='', flush=True)

                # Download
                file_path = await self.client.download_media(
                    message.media,
                    file=str(output_path),
                    progress_callback=progress_callback
                )

                print()  # New line after progress

                if file_path:
                    file_size = Path(file_path).stat().st_size
                    return {
                        'success': True,
                        'filename': file_path,
                        'filesize': format_bytes(file_size)
                    }
                else:
                    return {'success': False, 'error': 'Download failed'}
            else:
                return {'success': False, 'error': 'Unsupported media type'}

        except Exception as e:
            logger.error(f"Error downloading from Telegram: {e}")
            return {'success': False, 'error': str(e)}

    def download(self, url: str, **kwargs) -> Dict:
        """
        Download video từ Telegram

        Args:
            url: Telegram URL (t.me/channel/message_id)
            **kwargs:
                - output_dir: Thư mục output

        Returns:
            Dict với success, filename, error
        """
        output_dir = kwargs.get('output_dir', './downloads')

        # Run async function
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            result = loop.run_until_complete(self._download_video(url, output_dir))
            return result
        finally:
            # Properly disconnect client before closing loop
            if self.client:
                try:
                    loop.run_until_complete(self.client.disconnect())
                except:
                    pass
            loop.close()

    def get_available_formats(self, url: str) -> List[Dict]:
        """
        Telegram thường chỉ có 1 format
        """
        return [{
            'format_id': 'default',
            'height': 0,  # Unknown
            'fps': 30,
            'ext': 'mp4'
        }]

    def __del__(self):
        """Cleanup"""
        if self.client:
            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    loop.create_task(self.client.disconnect())
                else:
                    loop.run_until_complete(self.client.disconnect())
            except:
                pass
