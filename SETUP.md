# 🚀 Hướng Dẫn Cài Đặt - Setup Guide

Hướng dẫn chi tiết để cài đặt và cấu hình Video Downloader trên **Windows/WSL**.

## 📋 Yêu Cầu Hệ Thống

- **Windows 10/11** với WSL2 (Ubuntu 22.04 recommended)
- **Python 3.8+**
- **FFmpeg** (để merge video phân mảnh)
- **Git**
- **VS Code** (optional, nhưng khuyên dùng)

---

## 🐧 Phần 1: Cài Đặt WSL (Windows Subsystem for Linux)

### Bước 1: Kích Hoạt WSL

Mở **PowerShell** với quyền Administrator và chạy:

```powershell
wsl --install
```

Hoặc nếu đã có WSL1, upgrade lên WSL2:

```powershell
wsl --set-default-version 2
```

### Bước 2: Cài Ubuntu

```powershell
wsl --install -d Ubuntu-22.04
```

Sau khi cài xong, mở Ubuntu và tạo username/password.

### Bước 3: Cập Nhật Ubuntu

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 🐍 Phần 2: Cài Đặt Python

### Check Python Version

```bash
python3 --version
```

Nếu < 3.8, cài mới:

```bash
sudo apt install python3 python3-pip python3-venv -y
```

### Cài pip và venv

```bash
sudo apt install python3-pip python3-venv -y
```

---

## 🎬 Phần 3: Cài Đặt FFmpeg

FFmpeg cần thiết để merge video và audio, xử lý video phân mảnh.

### Cài FFmpeg trên WSL/Ubuntu

```bash
sudo apt install ffmpeg -y
```

### Verify Installation

```bash
ffmpeg -version
```

Phải hiện version ≥ 4.x

---

## 📦 Phần 4: Clone Project và Cài Dependencies

### Bước 1: Clone Repository

```bash
cd ~
mkdir -p projects/download
cd projects/download

# Clone từ GitHub
git clone https://github.com/trancn-dev/Download-video.git
cd Download-video
```

### Bước 2: Tạo Virtual Environment

```bash
# Tạo virtual environment
python3 -m venv venv

# Kích hoạt
source venv/bin/activate

# Lưu ý: Prompt sẽ có (venv) ở đầu
```

### Bước 3: Cài Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

⏳ Quá trình này mất ~2-5 phút.

### Bước 4: Verify Installation

```bash
# Check yt-dlp
yt-dlp --version

# Check các packages
pip list
```

---

## ⚙️ Phần 5: Cấu Hình

### Bước 1: Tạo File .env

```bash
cp .env.example .env
nano .env
```

### Bước 2: Chỉnh Sửa .env

```bash
# ==============================================
# TELEGRAM API (Optional - xem TELEGRAM_SETUP.md)
# ==============================================
TELEGRAM_API_ID=
TELEGRAM_API_HASH=
TELEGRAM_PHONE=

# ==============================================
# TWITTER/X (Optional - xem TWITTER_AUTH.md)
# ==============================================
# Để trống nếu chưa cần

# ==============================================
# DOWNLOAD SETTINGS
# ==============================================
DOWNLOAD_DIR=./downloads

# ==============================================
# WEB UI
# ==============================================
WEB_PORT=5000
WEB_HOST=0.0.0.0
WEB_DEBUG=False
```

Lưu file: `Ctrl+O`, `Enter`, `Ctrl+X`

### Bước 3: Tạo Thư Mục Downloads

```bash
mkdir -p downloads
```

---

## 🎯 Phần 6: Test Chạy Thử

### Test 1: CLI Download

```bash
# Download video public từ YouTube
./cli_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### Test 2: Web UI

```bash
# Chạy web server
./web_app.py
```

Mở browser và truy cập: **http://localhost:5000**

Nếu mở từ Windows: **http://localhost:5000**
Nếu mở từ máy khác: **http://YOUR_IP:5000**

---

## 🔧 Phần 7: Tips cho WSL Users

### 1. Truy Cập Files Windows từ WSL

```bash
# Windows C:\ = /mnt/c/
cd /mnt/c/Users/YourName/Downloads

# Copy file từ Windows sang WSL
cp /mnt/c/Users/YourName/Desktop/video.mp4 ~/projects/download/Download-video/downloads/
```

### 2. Truy Cập Files WSL từ Windows

Trong Windows Explorer, gõ:
```
\\wsl$\Ubuntu-22.04\home\username\projects\download\Download-video
```

Hoặc pin folder này vào Quick Access.

### 3. Mở VS Code trong WSL

```bash
# Từ thư mục project
code .
```

VS Code sẽ tự động mở với WSL extension.

### 4. Convert Paths

```bash
# Windows to WSL
# C:\Users\Name\file.txt → /mnt/c/Users/Name/file.txt

# WSL to Windows
# ~/projects → \\wsl$\Ubuntu-22.04\home\username\projects
```

### 5. Chọn Thư Mục Download Windows

```bash
# Download thẳng vào Downloads của Windows
./cli_downloader.py "URL" -o /mnt/c/Users/YourName/Downloads
```

---

## 🚨 Troubleshooting

### Lỗi: "FFmpeg not found"

```bash
# Check FFmpeg
which ffmpeg

# Nếu không có, cài lại
sudo apt update
sudo apt install ffmpeg -y
```

### Lỗi: "Python command not found"

```bash
# Dùng python3 thay vì python
python3 --version

# Hoặc tạo alias
echo "alias python=python3" >> ~/.bashrc
source ~/.bashrc
```

### Lỗi: "pip: command not found"

```bash
sudo apt install python3-pip -y
```

### Lỗi: "Permission denied" khi chạy .py

```bash
chmod +x cli_downloader.py
chmod +x web_app.py
```

### Lỗi: "Module not found"

```bash
# Đảm bảo venv đã activate
source venv/bin/activate

# Cài lại dependencies
pip install -r requirements.txt
```

### Lỗi: "Address already in use" (Port 5000)

```bash
# Đổi port trong .env
nano .env
# Thay WEB_PORT=5000 → WEB_PORT=8080

# Hoặc kill process đang dùng port 5000
sudo lsof -ti:5000 | xargs kill -9
```

### Lỗi: WSL quá chậm

```bash
# Restart WSL từ PowerShell (Windows)
wsl --shutdown
wsl
```

### Lỗi: "Cannot connect to Telegram"

Xem hướng dẫn chi tiết trong `TELEGRAM_SETUP.md`

### Lỗi: "Twitter protected tweet"

Xem hướng dẫn chi tiết trong `TWITTER_AUTH.md`

---

## 📱 Phần 8: Cài Extension Hữu Ích (Optional)

### VS Code Extensions

```bash
# Mở VS Code
code .

# Cài các extensions:
# - Python (Microsoft)
# - WSL (Microsoft)
# - GitLens
# - Pylance
```

### Browser Extensions (cho Twitter cookies)

- **Chrome/Edge:** Get cookies.txt LOCALLY
- **Firefox:** cookies.txt

Xem chi tiết trong `TWITTER_AUTH.md`

---

## 🎓 Phần 9: Sử Dụng Nâng Cao

### Auto-activate venv khi cd vào folder

```bash
nano ~/.bashrc

# Thêm vào cuối file:
cd_download() {
    cd ~/projects/download/Download-video
    source venv/bin/activate
}

# Lưu và reload
source ~/.bashrc

# Giờ chỉ cần gõ:
cd_download
```

### Tạo Alias

```bash
nano ~/.bashrc

# Thêm:
alias vdl='~/projects/download/Download-video/cli_downloader.py'
alias vdl-web='~/projects/download/Download-video/web_app.py'

# Lưu và reload
source ~/.bashrc

# Giờ có thể dùng:
vdl "https://youtube.com/..."
vdl-web
```

---

## 📚 Next Steps

1. ✅ **Cài đặt xong** → Test với video public
2. 📱 **Telegram setup** → Xem `TELEGRAM_SETUP.md`
3. 🐦 **Twitter setup** → Xem `TWITTER_AUTH.md`
4. 🎬 **Bắt đầu download!**

---

## 🆘 Support

Nếu gặp vấn đề:
1. Check lại từng bước
2. Đọc phần Troubleshooting
3. Check logs: `tail -f downloader.log`
4. Open issue trên GitHub

---

## 📖 Resources

- [WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)

---

Made with ❤️ by trancn-dev
