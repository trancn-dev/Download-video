# ⚡ QUICK START - Bắt Đầu Trong 2 Phút

## 🚀 Cài Đặt Nhanh

```bash
# Clone repo
git clone https://github.com/trancn-dev/Download-video.git
cd Download-video

# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Test ngay!
./cli_downloader.py "https://youtube.com/watch?v=dQw4w9WgXcQ"
```

## 🎯 Sử Dụng Cơ Bản

### CLI
```bash
# Download về thư mục hiện tại
./cli_downloader.py "URL"

# Chọn thư mục Windows Downloads (nếu dùng WSL)
./cli_downloader.py "URL" -o /mnt/c/Users/TenBan/Downloads

# Chọn chất lượng
./cli_downloader.py "URL" --quality

# Xem tất cả chất lượng
./cli_downloader.py "URL" --list-formats
```

### Web UI
```bash
./web_app.py
# Mở: http://localhost:5000
```

## 🐦 Twitter Protected Videos

1. Cài extension: "Get cookies.txt LOCALLY"
2. Đăng nhập Twitter/X
3. Export cookies.txt
4. Đặt file vào thư mục project
5. Done! Download protected videos

📖 Chi tiết: [TWITTER_AUTH.md](TWITTER_AUTH.md)

## 📱 Telegram Private Channels

1. Truy cập: https://my.telegram.org/apps
2. Tạo app, lấy API_ID và API_HASH
3. Thêm vào file .env
4. Done! Download private channels

📖 Chi tiết: [TELEGRAM_SETUP.md](TELEGRAM_SETUP.md)

## 🆘 Lỗi Thường Gặp

```bash
# FFmpeg not found
sudo apt install ffmpeg -y

# Module not found
source venv/bin/activate
pip install -r requirements.txt

# Permission denied
chmod +x cli_downloader.py web_app.py
```

## 📚 Đọc Thêm

- [README.md](README.md) - Overview đầy đủ
- [SETUP.md](SETUP.md) - Hướng dẫn chi tiết cho WSL/Windows
- [USAGE.md](USAGE.md) - Cách dùng và tips & tricks
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Tổng kết dự án

---

**Enjoy downloading! 🎬**
