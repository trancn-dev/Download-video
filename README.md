# 🎥 Video Downloader - Tải Video Đa Nền Tảng

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

Công cụ mạnh mẽ để tải video từ **X.com (Twitter)**, **Telegram** (bao gồm nhóm kín), và **1000+ websites** khác.

[Tính Năng](#-tính-năng-chính) • [Cài Đặt](#-cài-đặt-nhanh) • [Sử Dụng](#-cách-sử-dụng) • [Docs](#-documentation)

</div>

---

## ✨ Tính Năng Chính

### 🎯 Nền Tảng Hỗ Trợ

#### 🔥 Ưu Tiên
- ✅ **X.com (Twitter)**
  - Video public
  - Protected tweets (chỉ followers)
  - Private accounts
- ✅ **Telegram**
  - Public channels
  - Private groups (với API)
  - Media documents

#### 🌐 1000+ Sites Khác
- YouTube (videos, shorts, live)
- TikTok (không watermark)
- Instagram (reels, stories)
- Facebook (videos, reels)
- Reddit, Twitch, Vimeo
- ...và nhiều hơn nữa!

[→ Xem full list](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

### 🚀 Khả Năng Đặc Biệt

- 📹 **Video Phân Mảnh**: Tự động merge HLS/M3U8/DASH streams
- 🔴 **Live Streaming**: Download video đang live
- 🔓 **Bypass Protection**: Download video ẩn nút download
- 🎚️ **Chọn Chất Lượng**: Từ 144p đến 8K (nếu có)
- ⚡ **Multi-Download**: Tải đồng thời nhiều video
- 📊 **Progress Bar**: Theo dõi tiến trình real-time
- 🔄 **Auto-Resume**: Tiếp tục nếu bị ngắt
- 🔁 **Auto-Retry**: Tự động retry khi lỗi

### 🖥️ Giao Diện Linh Hoạt

#### ⌨️ CLI (Command Line)
```bash
./cli_downloader.py "URL" -o /path/folder
```
✅ Nhanh, mạnh mẽ | ✅ Chọn thư mục tùy ý | ✅ Dễ automation | ✅ Full control

#### 🌐 Web UI
```bash
./web_app.py
```
✅ Giao diện đẹp, dễ dùng | ✅ Không cần biết lệnh | ✅ Access từ mọi thiết bị | ✅ Share trong LAN

---

## 📦 Cài Đặt Nhanh

### ⚡ Quick Start (5 phút)

```bash
# 1. Clone repository
git clone https://github.com/trancn-dev/Download-video.git
cd Download-video

# 2. Cài đặt dependencies
python3 -m venv venv
source venv/bin/activate  # Linux/WSL
pip install -r requirements.txt

# 3. Cấu hình (optional)
cp .env.example .env

# 4. Test ngay!
./cli_downloader.py "https://youtube.com/watch?v=dQw4w9WgXcQ"
```

### 📋 Yêu Cầu Hệ Thống

- **Python 3.8+** - Required
- **FFmpeg** - Required (merge videos)
- **OS**: Linux/WSL - Windows qua WSL
- **RAM**: 2GB+ recommended
- **Disk**: 1GB+ for downloads

#### Cài FFmpeg
```bash
# Ubuntu/WSL
sudo apt install ffmpeg -y

# Verify
ffmpeg -version
```

### 🪟 Windows Users

Dự án này chạy tốt nhất trên **WSL (Windows Subsystem for Linux)**.

👉 **Xem hướng dẫn chi tiết:** [SETUP.md](SETUP.md)

---

## 🎮 Cách Sử Dụng

### 🖥️ CLI - Command Line

#### Basic Usage
```bash
# Download đơn giản
./cli_downloader.py "https://x.com/user/status/123456789"

# Chọn thư mục lưu (quan trọng cho WSL users!)
./cli_downloader.py "URL" -o /mnt/c/Users/YourName/Downloads

# Chọn chất lượng interactive
./cli_downloader.py "URL" --quality

# Sử dụng preset
./cli_downloader.py "URL" --preset high    # 1080p
./cli_downloader.py "URL" --preset medium  # 720p
```

#### Advanced Usage
```bash
# Xem tất cả formats có sẵn
./cli_downloader.py "URL" --list-formats

# Chỉ tải audio
./cli_downloader.py "URL" --audio-only

# Verbose mode (debug)
./cli_downloader.py "URL" -v
```

### 🌐 Web UI

```bash
# Khởi động server
./web_app.py

# Truy cập từ browser
# Local: http://localhost:5000
# LAN: http://YOUR_IP:5000
```

**Features Web UI:**
- 📋 Xem tất cả chất lượng có sẵn
- 🎚️ Chọn quality preset
- 📊 Progress tracking
- 💾 Download trực tiếp về máy

👉 **Xem chi tiết:** [USAGE.md](USAGE.md)

---

## ⚙️ Cấu Hình

### 📱 Telegram (Optional)

**Chỉ cần nếu:** Download từ Telegram private channels/groups

👉 **Setup guide:** [TELEGRAM_SETUP.md](TELEGRAM_SETUP.md)

### 🐦 Twitter/X (Optional)

**Chỉ cần nếu:** Download video protected (chỉ followers mới xem)

👉 **Setup guide:** [TWITTER_AUTH.md](TWITTER_AUTH.md)

---

## 🎬 Ví Dụ Thực Tế

### Twitter/X
```bash
# Public video
./cli_downloader.py "https://x.com/NASA/status/123456789"

# Protected tweet (cần cookies.txt)
./cli_downloader.py "https://x.com/protected_user/status/987654321"
```

### Telegram
```bash
# Public channel
./cli_downloader.py "https://t.me/durov/123"

# Private group (cần API credentials)
./cli_downloader.py "https://t.me/c/1234567890/999"
```

### YouTube
```bash
# Video thường
./cli_downloader.py "https://youtube.com/watch?v=dQw4w9WgXcQ"

# Shorts
./cli_downloader.py "https://youtube.com/shorts/abc123"
```

---

## 🔒 Bảo Mật & Privacy

### ⚠️ QUAN TRỌNG

**KHÔNG BAO GIỜ** commit các file sau lên Git:
- ❌ `.env` - Chứa credentials
- ❌ `cookies.txt` - Cookie browser của bạn
- ❌ `*.session` - Telegram session
- ❌ `downloads/` - Video đã tải

✅ Các file này đã được add vào `.gitignore`

---

## 🛠️ Troubleshooting

### Lỗi Thường Gặp

**FFmpeg not found**
```bash
sudo apt install ffmpeg -y
```

**Module not found**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**Permission denied**
```bash
chmod +x cli_downloader.py web_app.py
```

**Twitter protected tweet**
- Export `cookies.txt` từ browser
- Xem: [TWITTER_AUTH.md](TWITTER_AUTH.md)

**Telegram authentication**
- Setup Telegram API
- Xem: [TELEGRAM_SETUP.md](TELEGRAM_SETUP.md)

👉 **Xem thêm:** [SETUP.md - Troubleshooting](SETUP.md#-troubleshooting)

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [📖 README.md](README.md) | Overview (file này) |
| [🚀 SETUP.md](SETUP.md) | Hướng dẫn cài đặt chi tiết cho WSL/Windows |
| [🎯 USAGE.md](USAGE.md) | Hướng dẫn sử dụng, tips & tricks |
| [🐦 TWITTER_AUTH.md](TWITTER_AUTH.md) | Setup Twitter authentication |
| [📱 TELEGRAM_SETUP.md](TELEGRAM_SETUP.md) | Setup Telegram API |

---

## 📊 Project Structure

```
Download-video/
├── cli_downloader.py       # CLI interface
├── web_app.py              # Web UI server
├── core/                   # Core modules
│   ├── config.py           # Configuration
│   ├── utils.py            # Utilities
│   ├── base_downloader.py  # Base class
│   ├── generic_downloader.py
│   ├── twitter_downloader.py
│   ├── telegram_downloader.py
│   └── downloader_factory.py
├── templates/              # Web UI templates
│   └── index.html
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

---

## 🙏 Credits

Dự án này sử dụng các thư viện open-source tuyệt vời:

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Universal video downloader
- [Telethon](https://github.com/LonamiWebs/Telethon) - Telegram client
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [FFmpeg](https://ffmpeg.org/) - Video processing

---

## ⚖️ Disclaimer

Tool này được tạo ra cho **mục đích học tập và sử dụng cá nhân**.

- ✅ Sử dụng hợp pháp cho video của bạn
- ✅ Backup nội dung cá nhân
- ✅ Download với permission của tác giả
- ❌ **KHÔNG** vi phạm bản quyền
- ❌ **KHÔNG** phát tán nội dung trái phép
- ❌ **KHÔNG** sử dụng cho mục đích thương mại

**Bạn chịu trách nhiệm với việc sử dụng tool này!**

---

<div align="center">

**Made with ❤️ by [trancn-dev](https://github.com/trancn-dev)**

⭐ Star this repo if you find it useful!

</div>
