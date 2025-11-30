# 🎬 Hướng Dẫn Sử Dụng Nhanh

## ✅ Môi Trường Đã Cài Đặt Xong!

Bạn đã có:
- ✅ Python 3.10.12
- ✅ pip 25.3
- ✅ FFmpeg 4.4.2
- ✅ Virtual environment với tất cả dependencies
- ✅ Project hoàn chỉnh với CLI và Web UI

---

## 🚀 Cách Sử Dụng

### 1️⃣ Dùng CLI (Command Line)

```bash
# Activate virtual environment
source venv/bin/activate

# Download video (chất lượng tốt nhất)
python cli_downloader.py "URL_VIDEO"

# Chọn thư mục lưu
python cli_downloader.py "URL_VIDEO" -o /mnt/c/Users/YourName/Downloads

# Chọn chất lượng
python cli_downloader.py "URL_VIDEO" --quality high

# Xem tất cả format có sẵn
python cli_downloader.py "URL_VIDEO" --list-formats
```

### 2️⃣ Dùng Web UI (Giao Diện Web)

```bash
# Khởi động web server
./start_web.sh

# Hoặc:
source venv/bin/activate
python web_app.py
```

Sau đó mở trình duyệt:
- **http://localhost:5000**

---

## 📦 Các Nền Tảng Được Hỗ Trợ

### ✅ Đang hoạt động ngay (không cần setup thêm):
- YouTube (1000+ sites khác qua yt-dlp)
- Facebook
- Instagram
- TikTok
- Reddit
- Dailymotion
- Vimeo
- ...và hơn 1000 sites khác

### ⚙️ Cần setup thêm:

#### 🐦 **Twitter/X (Protected Tweets)**
1. Cài extension: "Get cookies.txt LOCALLY"
2. Đăng nhập Twitter/X trên browser
3. Export cookies
4. Lưu file `cookies.txt` vào thư mục project

👉 Xem chi tiết: [TWITTER_AUTH.md](TWITTER_AUTH.md)

#### 📱 **Telegram (Private Groups)**
1. Truy cập: https://my.telegram.org/apps
2. Tạo app và lấy API_ID, API_HASH
3. Thêm vào file `.env`:
```bash
TELEGRAM_API_ID=12345678
TELEGRAM_API_HASH=abcdef1234567890
TELEGRAM_PHONE=+84912345678
```

👉 Xem chi tiết: [TELEGRAM_SETUP.md](TELEGRAM_SETUP.md)

---

## 🎯 Ví Dụ Nhanh

### YouTube:
```bash
python cli_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### TikTok:
```bash
python cli_downloader.py "https://www.tiktok.com/@user/video/1234567890"
```

### Instagram:
```bash
python cli_downloader.py "https://www.instagram.com/p/ABC123/"
```

### Facebook:
```bash
python cli_downloader.py "https://www.facebook.com/watch/?v=1234567890"
```

---

## 🔧 Cấu Hình Nâng Cao

Chỉnh sửa file `.env`:

```bash
# Thư mục lưu mặc định
DOWNLOAD_DIR=./downloads

# Lưu vào Windows Downloads từ WSL
DOWNLOAD_DIR=/mnt/c/Users/YourName/Downloads

# Chất lượng mặc định
DEFAULT_QUALITY=best

# Port web UI
WEB_PORT=5000
```

---

## 📂 Cấu Trúc File

```
Download-video/
├── cli_downloader.py      # CLI tool
├── web_app.py            # Web UI server
├── start_web.sh          # Script khởi động web
├── .env                  # Cấu hình (edit ở đây)
├── requirements.txt      # Dependencies đã cài
├── downloads/            # Thư mục lưu video mặc định
├── core/                 # Core modules
└── templates/            # Web UI template
```

---

## 🐛 Troubleshooting

### Video không tải được?
```bash
# Thử với --list-formats để xem format
python cli_downloader.py "URL" --list-formats

# Chọn format cụ thể
python cli_downloader.py "URL" --quality medium
```

### Twitter/X protected video?
- Cần export cookies.txt (xem TWITTER_AUTH.md)

### Telegram private group?
- Cần setup API credentials (xem TELEGRAM_SETUP.md)

### Port 5000 đã được dùng?
```bash
# Đổi port trong .env
WEB_PORT=8080
```

---

## 📚 Tài Liệu Chi Tiết

- **README.md** - Tổng quan dự án
- **SETUP.md** - Hướng dẫn cài đặt chi tiết
- **USAGE.md** - Hướng dẫn sử dụng đầy đủ
- **TWITTER_AUTH.md** - Setup Twitter authentication
- **TELEGRAM_SETUP.md** - Setup Telegram API
- **PROJECT_SUMMARY.md** - Tóm tắt kỹ thuật

---

## 💡 Tips & Tricks

### Lưu video vào Windows từ WSL:
```bash
# Downloads folder
python cli_downloader.py "URL" -o /mnt/c/Users/YourName/Downloads

# Desktop
python cli_downloader.py "URL" -o /mnt/c/Users/YourName/Desktop
```

### Download nhiều video:
```bash
# Tạo file urls.txt với mỗi URL trên 1 dòng
while read url; do
    python cli_downloader.py "$url"
done < urls.txt
```

### Alias nhanh (thêm vào ~/.bashrc):
```bash
alias dl='cd ~/projects/download/Download-video && source venv/bin/activate && python cli_downloader.py'
alias dlweb='cd ~/projects/download/Download-video && ./start_web.sh'
```

Sau đó:
```bash
dl "URL_VIDEO"
dlweb  # Khởi động web UI
```

---

## 🆘 Support

Gặp vấn đề? Xem thêm:
- QUICKSTART.md
- SETUP.md
- USAGE.md

Hoặc check logs trong terminal để biết lỗi cụ thể.

---

## ⚡ Quick Commands Cheatsheet

```bash
# Activate venv
source venv/bin/activate

# Download video
python cli_downloader.py "URL"

# Start web UI
./start_web.sh

# List formats
python cli_downloader.py "URL" --list-formats

# Choose quality
python cli_downloader.py "URL" --quality high

# Custom output directory
python cli_downloader.py "URL" -o /path/to/folder

# Deactivate venv
deactivate
```

---

**🎉 Enjoy downloading! 🎥**
