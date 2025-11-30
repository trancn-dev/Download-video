# 🎯 Hướng Dẫn Sử Dụng Nhanh

## 📱 Chạy trên điện thoại/khi không có máy tính

Dự án này chạy trên **WSL/Linux** nên bạn cần máy tính để chạy. Tuy nhiên, bạn có thể:

### Option 1: Deploy lên VPS/Cloud
- Deploy lên VPS Ubuntu
- Chạy web UI và access từ điện thoại
- Port forward: `http://your-vps-ip:5000`

### Option 2: Sử dụng Termux (Android)
```bash
# Cài Termux từ F-Droid
pkg update && pkg upgrade
pkg install python git ffmpeg
git clone https://github.com/trancn-dev/Download-video
cd Download-video
pip install -r requirements.txt
python web_app.py
```

---

## 🚀 Cách Sử Dụng CLI

### Download cơ bản
```bash
./cli_downloader.py "https://youtube.com/watch?v=..."
```

### Chọn thư mục lưu
```bash
# Lưu vào Desktop (Windows)
./cli_downloader.py "URL" -o /mnt/c/Users/YourName/Desktop

# Lưu vào Downloads (Windows)
./cli_downloader.py "URL" -o /mnt/c/Users/YourName/Downloads

# Lưu vào thư mục tùy chọn
./cli_downloader.py "URL" -o /path/to/folder
```

### Chọn chất lượng video
```bash
# Hiện menu chọn chất lượng
./cli_downloader.py "URL" --quality

# Hoặc dùng preset
./cli_downloader.py "URL" --preset high    # 1080p
./cli_downloader.py "URL" --preset medium  # 720p
./cli_downloader.py "URL" --preset low     # 480p
```

### Xem tất cả chất lượng có sẵn
```bash
./cli_downloader.py "URL" --list-formats
```

### Chỉ tải audio
```bash
./cli_downloader.py "URL" --audio-only
```

---

## 🌐 Cách Sử Dụng Web UI

### Khởi động Web Server
```bash
./web_app.py

# Hoặc nếu muốn đổi port
WEB_PORT=8080 ./web_app.py
```

### Truy cập
- Từ máy local: `http://localhost:5000`
- Từ máy khác trong LAN: `http://YOUR_IP:5000`

### Sử dụng Web UI
1. Paste URL video vào ô input
2. Tool sẽ tự động detect platform
3. Click "Xem Tất Cả Chất Lượng" để xem formats
4. Chọn chất lượng từ dropdown
5. Click "Download Video"
6. Đợi xử lý xong
7. Click "Tải File Xuống" để download về máy

---

## 🎬 Ví Dụ Thực Tế

### 1. Download từ Twitter/X (Public)
```bash
./cli_downloader.py "https://x.com/user/status/123456789"
```

### 2. Download từ Twitter/X (Protected - cần cookies)
```bash
# Đảm bảo đã có cookies.txt (xem TWITTER_AUTH.md)
./cli_downloader.py "https://x.com/protected_user/status/123456789"
```

### 3. Download từ Telegram
```bash
# Public channel
./cli_downloader.py "https://t.me/channel_name/123"

# Private channel (cần setup API - xem TELEGRAM_SETUP.md)
./cli_downloader.py "https://t.me/c/1234567890/123"
```

### 4. Download từ YouTube
```bash
# Video thường
./cli_downloader.py "https://youtube.com/watch?v=dQw4w9WgXcQ"

# Shorts
./cli_downloader.py "https://youtube.com/shorts/abc123"

# Playlist (download từng video)
./cli_downloader.py "https://youtube.com/playlist?list=..."
```

### 5. Download từ TikTok
```bash
./cli_downloader.py "https://tiktok.com/@user/video/123456789"
```

### 6. Download từ Instagram
```bash
# Reel
./cli_downloader.py "https://instagram.com/reel/..."

# Post có video
./cli_downloader.py "https://instagram.com/p/..."
```

### 7. Download từ Facebook
```bash
./cli_downloader.py "https://facebook.com/watch/?v=123456789"
```

---

## 🔍 Các Platform Hỗ Trợ

### ✅ Đã Test và Hoạt Động Tốt:
- **Twitter/X** (public & protected)
- **YouTube** (video, shorts, live)
- **TikTok**
- **Instagram** (reels, videos)
- **Facebook**
- **Reddit**
- **Telegram** (public & private with API)

### 🎯 Hỗ Trợ Qua yt-dlp (1000+ sites):
- Twitch
- Vimeo
- Dailymotion
- Bilibili
- SoundCloud
- Bandcamp
- và nhiều sites khác...

Xem full list: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

---

## ⚙️ Tips & Tricks

### 1. Download nhiều video cùng lúc
```bash
# Tạo file urls.txt
echo "https://youtube.com/watch?v=..." > urls.txt
echo "https://x.com/user/status/..." >> urls.txt

# Download từng URL
while read url; do
    ./cli_downloader.py "$url" -o ./downloads
done < urls.txt
```

### 2. Tự động đổi tên file
```bash
# Download và đổi tên
./cli_downloader.py "URL" -o ./downloads && \
mv downloads/*.mp4 "MyVideo_$(date +%Y%m%d).mp4"
```

### 3. Check disk space trước khi download
```bash
df -h /mnt/c/Users/YourName/Downloads
```

### 4. Download video dài với quality cao
```bash
# Sử dụng medium/low để tiết kiệm dung lượng
./cli_downloader.py "URL" --preset medium
```

### 5. Resume download nếu bị ngắt
yt-dlp tự động hỗ trợ resume. Chỉ cần chạy lại command.

---

## 🚨 Xử Lý Lỗi Thường Gặp

### 1. "FFmpeg not found"
```bash
sudo apt install ffmpeg -y
```

### 2. "Module not found"
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### 3. "Permission denied"
```bash
chmod +x cli_downloader.py web_app.py
```

### 4. "Invalid URL"
Check lại URL, đảm bảo có `https://`

### 5. "Video not available"
- Video đã bị xóa
- Video bị geo-restriction
- Cần authentication (xem TWITTER_AUTH.md, TELEGRAM_SETUP.md)

### 6. "Disk full"
```bash
# Check space
df -h

# Dọn dẹp downloads cũ
rm -rf downloads/*.mp4
```

---

## 📊 So Sánh CLI vs Web UI

| Feature | CLI | Web UI |
|---------|-----|--------|
| Tốc độ | ⚡ Nhanh hơn | 🐢 Chậm hơn 1 chút |
| Chọn thư mục | ✅ Linh hoạt | ❌ Fixed folder |
| UI/UX | ⌨️ Terminal | 🖱️ Giao diện đẹp |
| Remote access | ❌ Không | ✅ Có (qua LAN) |
| Automation | ✅ Dễ script | ❌ Khó |
| List formats | ✅ Chi tiết | ✅ Đơn giản |

### Khi nào dùng CLI?
- Download nhiều video
- Cần chọn thư mục cụ thể
- Script automation
- Dùng quen terminal

### Khi nào dùng Web UI?
- Download thỉnh thoảng
- Thích giao diện đẹp
- Chia sẻ cho người khác dùng (LAN)
- Dùng từ điện thoại/tablet

---

## 📚 Xem Thêm

- **README.md** - Tổng quan project
- **SETUP.md** - Hướng dẫn cài đặt chi tiết
- **TWITTER_AUTH.md** - Setup Twitter authentication
- **TELEGRAM_SETUP.md** - Setup Telegram API

---

Made with ❤️ by trancn-dev
