# 🎥 Video Downloader - Tải Video Đa Nền Tảng

Công cụ mạnh mẽ để tải video từ **X.com (Twitter)**, **Telegram** (bao gồm nhóm kín), và **1000+ websites** khác. Hỗ trợ video live, video phân mảnh (HLS/M3U8/DASH), và video bị ẩn nút download.

## ✨ Tính Năng Chính

### 🎯 Nền Tảng Hỗ Trợ
- **X.com (Twitter)**: Video private (chỉ người theo dõi mới xem), protected tweets
- **Telegram**: Nhóm kín, private channels, cần authentication
- **1000+ Sites**: YouTube, Facebook, Instagram, TikTok, Reddit, Twitch, và nhiều hơn nữa (powered by yt-dlp)

### 🚀 Khả Năng
- ✅ Tải video phân mảnh (HLS/M3U8/DASH) - tự động merge
- ✅ Video live streaming
- ✅ Bypass video ẩn nút download
- ✅ Chọn chất lượng video (từ thấp đến 4K/8K nếu có)
- ✅ Download đồng thời nhiều video
- ✅ Progress bar real-time
- ✅ Resume download nếu bị ngắt
- ✅ Auto-retry khi lỗi network

### 🖥️ Giao Diện
- **CLI (Command Line)**: Nhanh, mạnh mẽ, chọn thư mục lưu tùy ý
- **Web UI**: Giao diện đơn giản, paste link và download

## 📦 Cài Đặt

### Yêu Cầu Hệ Thống
- **Python 3.8+**
- **FFmpeg** (để merge video phân mảnh)
- **WSL** (nếu dùng Windows) - Xem chi tiết trong SETUP.md

### Cài Đặt Nhanh

```bash
# Clone repository
git clone https://github.com/trancn-dev/Download-video.git
cd Download-video

# Tạo virtual environment (khuyên dùng)
python3 -m venv venv
source venv/bin/activate  # Linux/WSL

# Cài dependencies
pip install -r requirements.txt

# Copy file config
cp .env.example .env

# Chỉnh sửa .env với thông tin của bạn
nano .env
```

## 🎮 Cách Sử Dụng

### CLI (Command Line Interface)

```bash
# Download cơ bản
python cli_downloader.py "https://x.com/username/status/123456789"

# Chọn chất lượng video
python cli_downloader.py "URL" --quality

# Tùy chỉnh thư mục lưu
python cli_downloader.py "URL" -o /path/to/folder

# List tất cả chất lượng
python cli_downloader.py "URL" --list-formats
```

### Web UI

```bash
# Chạy web server
python web_app.py

# Truy cập: http://localhost:5000
```

## ⚙️ Cấu Hình

### Setup Telegram
Xem chi tiết trong TELEGRAM_SETUP.md (sẽ tạo sau)

### Setup Twitter/X
Xem chi tiết trong TWITTER_AUTH.md (sẽ tạo sau)

## 🔒 Bảo Mật

⚠️ **KHÔNG commit các file sau lên Git:**
- .env
- cookies.txt
- *.session files
- downloads/

## 🛠️ Troubleshooting

### FFmpeg not found
```bash
sudo apt install ffmpeg  # Ubuntu/WSL
```

### Invalid API credentials
- Kiểm tra .env file
- Xem hướng dẫn setup

## 📚 Documentation

- SETUP.md - Cài đặt chi tiết
- TELEGRAM_SETUP.md - Telegram API
- TWITTER_AUTH.md - Twitter authentication

## ⚖️ Disclaimer

Tool dùng cho mục đích học tập và cá nhân. Tôn trọng bản quyền!

---

Made with ❤️ by trancn-dev
