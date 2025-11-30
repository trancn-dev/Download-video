# 🎬 Hướng Dẫn Sử Dụng Video Downloader

## 📋 Mục Lục
1. [Download Video Đơn Lẻ](#download-video-đơn-lẻ)
2. [Download Toàn Bộ X/Twitter Profile](#download-toàn-bộ-xtwitter-profile)
3. [Web Interface](#web-interface)
4. [Cấu Trúc Thư Mục](#cấu-trúc-thư-mục)

---

## 🎯 Download Video Đơn Lẻ

Dùng file: **`cli_downloader.py`**

### Cú Pháp Cơ Bản:
```bash
# Activate virtual environment
source venv/bin/activate

# Download video
python cli_downloader.py "URL_VIDEO"
```

### Các Nền Tảng Hỗ Trợ:
- ✅ **YouTube** (1000+ sites qua yt-dlp)
- ✅ **Telegram** (public & private channels)
- ✅ **X/Twitter** (single tweets)
- ✅ **TikTok**
- ✅ **Instagram**
- ✅ **Facebook**
- ✅ **Reddit, Vimeo, Dailymotion...**

### Ví Dụ:

#### YouTube:
```bash
python cli_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

#### Telegram:
```bash
# Public channel
python cli_downloader.py "https://t.me/channel_name/123"

# Private channel (cần đăng nhập)
python cli_downloader.py "https://t.me/c/1321440852/1421"
```

#### X/Twitter (Single Tweet):
```bash
python cli_downloader.py "https://x.com/user/status/1234567890"
```

#### TikTok:
```bash
python cli_downloader.py "https://www.tiktok.com/@user/video/1234567890"
```

#### Instagram:
```bash
python cli_downloader.py "https://www.instagram.com/p/ABC123/"
```

### Tùy Chọn Nâng Cao:

#### Chọn Chất Lượng:
```bash
# Preset chất lượng
python cli_downloader.py "URL" --preset best    # Tốt nhất (mặc định)
python cli_downloader.py "URL" --preset high    # Cao (1080p)
python cli_downloader.py "URL" --preset medium  # Trung bình (720p)
python cli_downloader.py "URL" --preset low     # Thấp (480p)
```

#### Chọn Thư Mục Lưu:
```bash
# Lưu vào thư mục khác
python cli_downloader.py "URL" -o /path/to/folder

# Lưu vào Windows từ WSL
python cli_downloader.py "URL" -o /mnt/c/Users/YourName/Downloads
```

#### Xem Tất Cả Format:
```bash
python cli_downloader.py "URL" --list-formats
```

#### Chỉ Tải Audio:
```bash
python cli_downloader.py "URL" --audio-only
```

### Thư Mục Lưu (Tự Động):
```
downloads/
├── youtube/        # Video YouTube
├── telegram/       # Video Telegram (single messages)
├── twitter/        # Video Twitter/X đơn lẻ (single tweets)
├── tiktok/         # Video TikTok
├── instagram/      # Video Instagram
├── facebook/       # Video Facebook
├── x/              # X/Twitter PROFILE downloads (toàn bộ)
│   ├── username1/
│   └── username2/
└── [platform]/     # Các nền tảng khác
```

---

## 🐦 Download Toàn Bộ X/Twitter Profile

Dùng file: **`download_x_profile.py`**

### Cú Pháp:
```bash
# Activate virtual environment
source venv/bin/activate

# Download tất cả media từ profile
python download_x_profile.py https://x.com/username

# Hoặc chỉ username
python download_x_profile.py username
```

### Ví Dụ:
```bash
# Download toàn bộ media của @duc9104
python download_x_profile.py https://x.com/duc9104

# Download profile @elonmusk
python download_x_profile.py elonmusk
```

### Tính Năng:
- ✅ Tải **TẤT CẢ** images và videos từ profile (không giới hạn)
- ✅ Bao gồm cả **retweets** (bài đăng lại từ user khác)
- ✅ Tự động tạo thư mục: `downloads/x/{username}/`
- ✅ Skip file đã tải (không download lại)
- ✅ Retry tự động khi lỗi (5 lần)
- ✅ Rate limiting (tránh bị block)

### Thư Mục Lưu:
```
downloads/
└── x/
    ├── duc9104/
    │   ├── 1234567890_1.jpg
    │   ├── 1234567890_2.mp4
    │   └── ...
    ├── elonmusk/
    │   └── ...
    └── [username]/
```

### Yêu Cầu:
⚠️ **Cần file `cookies.txt`** để download profile

**Cách Export Cookies:**
1. Cài extension "Get cookies.txt LOCALLY" (Chrome/Firefox)
2. Đăng nhập **x.com** trên browser
3. Click extension → Export → Lưu `cookies.txt`
4. Copy vào thư mục project:
   ```bash
   cp ~/Downloads/cookies.txt /home/trancn/projects/download/Download-video/
   ```

### List Files Đã Download:
```bash
python download_x_profile.py username --list
```

---

## 🌐 Web Interface

Dùng file: **`web_app.py`**

### Khởi Động Web UI:
```bash
# Cách 1: Script tự động
./start_web.sh

# Cách 2: Thủ công
source venv/bin/activate
python web_app.py
```

### Truy Cập:
Mở trình duyệt:
- http://localhost:5000
- http://127.0.0.1:5000

### Tính Năng Web UI:
- ✅ Giao diện đẹp, responsive
- ✅ Paste URL và download
- ✅ Xem danh sách format
- ✅ Chọn chất lượng
- ✅ Theo dõi tiến độ real-time
- ✅ Download từ bất kỳ nền tảng nào

---

## 📂 Cấu Trúc Thư Mục

```
Download-video/
├── cli_downloader.py          # Download video đơn lẻ
├── download_x_profile.py      # Download toàn bộ X profile
├── web_app.py                 # Web interface
├── start_web.sh               # Script khởi động web
├── cookies.txt                # Cookies cho X/Twitter
├── .env                       # Cấu hình
├── requirements.txt           # Dependencies
│
├── downloads/                 # Video downloads
│   ├── youtube/
│   ├── telegram/
│   ├── twitter/              # Single tweets
│   ├── tiktok/
│   ├── instagram/
│   ├── facebook/
│   └── x/                    # Profile downloads ⭐
│       ├── duc9104/
│       ├── elonmusk/
│       └── ...
│
├── core/                      # Core modules
│   ├── config.py
│   ├── utils.py
│   ├── base_downloader.py
│   ├── generic_downloader.py
│   ├── twitter_downloader.py
│   └── telegram_downloader.py
│
└── templates/
    └── index.html            # Web UI template
```

---

## ⚙️ Cấu Hình (.env)

### Telegram (Optional - chỉ cần nếu download private channels):
```bash
TELEGRAM_API_ID=12345678
TELEGRAM_API_HASH=abcdef1234567890
TELEGRAM_PHONE=+84912345678
```
👉 Xem: `TELEGRAM_SETUP.md`

### Twitter/X (Optional - cho protected accounts):
```bash
TWITTER_AUTH_TOKEN=Bearer ABC...
```
👉 Xem: `TWITTER_AUTH.md`

### Download Settings:
```bash
DOWNLOAD_DIR=./downloads
DEFAULT_QUALITY=best
MAX_CONCURRENT_DOWNLOADS=3
```

### Web UI:
```bash
WEB_PORT=5000
WEB_HOST=0.0.0.0
WEB_DEBUG=False
```

---

## 🚀 Quick Start Cheatsheet

```bash
# 1. Activate environment
source venv/bin/activate

# 2. Download single video
python cli_downloader.py "URL"

# 3. Download X profile
python download_x_profile.py https://x.com/username

# 4. Start web UI
./start_web.sh

# 5. Deactivate environment
deactivate
```

---

## 💡 Tips & Tricks

### Alias Nhanh (thêm vào ~/.bashrc):
```bash
alias dl='cd ~/projects/download/Download-video && source venv/bin/activate && python cli_downloader.py'
alias dlx='cd ~/projects/download/Download-video && source venv/bin/activate && python download_x_profile.py'
alias dlweb='cd ~/projects/download/Download-video && ./start_web.sh'
```

Sau đó:
```bash
dl "https://youtube.com/watch?v=..."
dlx elonmusk
dlweb
```

### Download Nhiều Video (Batch):
```bash
# Tạo file urls.txt với mỗi URL trên 1 dòng
while read url; do
    python cli_downloader.py "$url"
done < urls.txt
```

### Lưu Vào Windows từ WSL:
```bash
# Downloads folder
python cli_downloader.py "URL" -o /mnt/c/Users/YourName/Downloads

# Desktop
python cli_downloader.py "URL" -o /mnt/c/Users/YourName/Desktop/Videos
```

### Chuyển MOV sang MP4:
```bash
cd downloads/telegram
ffmpeg -i video.MOV -c copy video.mp4
```

---

## 🔧 Troubleshooting

### Video không tải được?
```bash
# Xem available formats
python cli_downloader.py "URL" --list-formats

# Chọn format khác
python cli_downloader.py "URL" --preset medium
```

### X/Twitter profile không download được?
- ✅ Kiểm tra file `cookies.txt` có tồn tại
- ✅ Cookies phải mới (đăng nhập lại nếu cần)
- ✅ Profile phải public hoặc bạn đã follow

### Telegram không connect được?
- ✅ Kiểm tra `.env` có đủ `TELEGRAM_API_ID`, `TELEGRAM_API_HASH`, `TELEGRAM_PHONE`
- ✅ Xem `TELEGRAM_SETUP.md` để lấy credentials

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
- **TELEGRAM_SETUP.md** - Setup Telegram API
- **TWITTER_AUTH.md** - Setup Twitter authentication
- **HUONG_DAN_NHANH.md** - Quick guide tiếng Việt

---

## 🎉 Tóm Tắt Nhanh

| Mục Đích | Command | Output |
|----------|---------|--------|
| Download 1 video | `python cli_downloader.py "URL"` | `downloads/{platform}/` |
| Download X profile | `python download_x_profile.py username` | `downloads/x/{username}/` |
| Web UI | `./start_web.sh` | http://localhost:5000 |
| List formats | `python cli_downloader.py "URL" --list-formats` | Hiển thị formats |
| Custom quality | `python cli_downloader.py "URL" --preset high` | Video chất lượng cao |

---

**Made with ❤️ by trancn-dev**
