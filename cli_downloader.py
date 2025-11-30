#!/usr/bin/env python3
"""
CLI Video Downloader - Tải video từ nhiều nền tảng
Hỗ trợ: Twitter/X, Telegram, YouTube, và 1000+ sites khác
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

from core.utils import (
    detect_platform,
    ensure_dir,
    is_valid_url,
    logger
)
from core.config import DEFAULT_DOWNLOAD_DIR, QUALITY_PRESETS
from core.downloader_factory import get_downloader

# Load environment variables
load_dotenv()


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='🎥 Video Downloader - Tải video từ nhiều nền tảng',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ:
  %(prog)s "https://x.com/user/status/123456789"
  %(prog)s "https://t.me/channel/123" --quality
  %(prog)s "URL" -o /path/to/folder
  %(prog)s "URL" --list-formats
        """
    )

    parser.add_argument(
        'url',
        help='URL của video cần tải'
    )

    parser.add_argument(
        '-o', '--output',
        default=DEFAULT_DOWNLOAD_DIR,
        help=f'Thư mục lưu video (mặc định: {DEFAULT_DOWNLOAD_DIR})'
    )

    parser.add_argument(
        '-q', '--quality',
        action='store_true',
        help='Cho phép chọn chất lượng video'
    )

    parser.add_argument(
        '--list-formats',
        action='store_true',
        help='Liệt kê tất cả chất lượng có sẵn'
    )

    parser.add_argument(
        '--preset',
        choices=list(QUALITY_PRESETS.keys()),
        help='Preset chất lượng: best, high, medium, low'
    )

    parser.add_argument(
        '--audio-only',
        action='store_true',
        help='Chỉ tải audio'
    )

    parser.add_argument(
        '--no-merge',
        action='store_true',
        help='Không merge video và audio'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Hiển thị thông tin chi tiết'
    )

    return parser.parse_args()


def list_available_formats(downloader, url: str):
    """Liệt kê tất cả format có sẵn"""
    print("\n📋 Đang lấy thông tin video...")

    try:
        formats = downloader.get_available_formats(url)

        if not formats:
            print("❌ Không tìm thấy format nào!")
            return

        print(f"\n✅ Tìm thấy {len(formats)} format:\n")
        print(f"{'ID':<8} {'Quality':<12} {'FPS':<6} {'Size':<12} {'Type':<10}")
        print("-" * 60)

        for fmt in formats:
            format_id = fmt.get('format_id', 'N/A')
            height = fmt.get('height', 0)
            fps = fmt.get('fps', 30)
            filesize = fmt.get('filesize', 0)
            vcodec = fmt.get('vcodec', 'unknown')

            quality = f"{height}p" if height > 0 else "audio"
            size_str = f"{filesize / 1024 / 1024:.1f} MB" if filesize else "Unknown"
            type_str = "video+audio" if fmt.get('acodec') != 'none' else "video only"

            print(f"{format_id:<8} {quality:<12} {fps:<6} {size_str:<12} {type_str:<10}")

        print("\n💡 Sử dụng --preset để chọn preset chất lượng")

    except Exception as e:
        logger.error(f"Lỗi khi lấy danh sách format: {e}")
        print(f"❌ Lỗi: {e}")


def select_quality_interactive(downloader, url: str) -> Optional[str]:
    """Chọn chất lượng video tương tác"""
    print("\n📋 Đang lấy thông tin video...")

    try:
        formats = downloader.get_available_formats(url)

        if not formats:
            print("❌ Không tìm thấy format nào!")
            return None

        # Lọc và sắp xếp video formats
        video_formats = [f for f in formats if f.get('height', 0) > 0]
        video_formats.sort(key=lambda x: x.get('height', 0), reverse=True)

        print("\n🎬 Chất lượng có sẵn:\n")
        for idx, fmt in enumerate(video_formats, 1):
            height = fmt.get('height', 0)
            fps = fmt.get('fps', 30)
            filesize = fmt.get('filesize', 0)
            size_str = f" ({filesize / 1024 / 1024:.1f} MB)" if filesize else ""

            print(f"  {idx}. {height}p @ {fps}fps{size_str}")

        print(f"  0. Best quality (mặc định)")

        while True:
            try:
                choice = input("\n👉 Chọn chất lượng (0-{}): ".format(len(video_formats)))

                if not choice:
                    return None  # Best quality

                choice_num = int(choice)

                if choice_num == 0:
                    return None  # Best quality
                elif 1 <= choice_num <= len(video_formats):
                    selected = video_formats[choice_num - 1]
                    return selected.get('format_id')
                else:
                    print("❌ Lựa chọn không hợp lệ!")
            except ValueError:
                print("❌ Vui lòng nhập số!")
            except KeyboardInterrupt:
                print("\n\n⚠️ Đã hủy!")
                sys.exit(0)

    except Exception as e:
        logger.error(f"Lỗi khi chọn chất lượng: {e}")
        return None


def main():
    """Main function"""
    args = parse_arguments()

    # Validate URL
    if not is_valid_url(args.url):
        print(f"❌ URL không hợp lệ: {args.url}")
        sys.exit(1)

    # Detect platform
    platform = detect_platform(args.url)
    print(f"\n🔍 Phát hiện nền tảng: {platform.upper()}")

    # Ensure output directory exists
    output_dir = ensure_dir(args.output)
    print(f"📁 Thư mục lưu: {output_dir}")

    # Get appropriate downloader
    try:
        downloader = get_downloader(platform)
    except Exception as e:
        print(f"❌ Lỗi khởi tạo downloader: {e}")
        sys.exit(1)

    # List formats mode
    if args.list_formats:
        list_available_formats(downloader, args.url)
        return

    # Select quality
    format_id = None
    if args.quality:
        format_id = select_quality_interactive(downloader, args.url)

    # Download options
    options = {
        'output_dir': str(output_dir),
        'audio_only': args.audio_only,
        'merge': not args.no_merge,
        'verbose': args.verbose
    }

    if format_id:
        options['format_id'] = format_id
    elif args.preset:
        options['preset'] = args.preset

    # Start download
    print("\n⬇️  Bắt đầu tải...\n")

    try:
        result = downloader.download(args.url, **options)

        if result['success']:
            print(f"\n✅ Tải thành công!")
            print(f"📦 File: {result['filename']}")
            if result.get('filesize'):
                print(f"📊 Size: {result['filesize']}")
        else:
            print(f"\n❌ Tải thất bại: {result.get('error', 'Unknown error')}")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\n⚠️ Đã hủy tải!")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Lỗi khi tải: {e}", exc_info=args.verbose)
        print(f"\n❌ Lỗi: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
