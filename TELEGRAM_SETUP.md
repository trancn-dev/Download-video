# 📱 Hướng Dẫn Setup Telegram API

Để download video từ Telegram (đặc biệt là từ private channels/groups), bạn cần có Telegram API credentials.

## 🔑 Lấy API Credentials

### Bước 1: Đăng Ký Telegram App

1. Truy cập: https://my.telegram.org/auth
2. Đăng nhập với số điện thoại Telegram của bạn
3. Nhập verification code từ Telegram app

### Bước 2: Tạo Application

1. Click vào **"API development tools"**
2. Điền thông tin:
   - **App title**: Tên app của bạn (VD: "My Video Downloader")
   - **Short name**: Tên ngắn (VD: "videodownloader")
   - **Platform**: Chọn "Desktop"
   - **Description**: Mô tả ngắn (optional)

3. Click **"Create application"**

### Bước 3: Lưu Credentials

Sau khi tạo, bạn sẽ nhận được:
- **api_id**: Một số (VD: 12345678)
- **api_hash**: Một chuỗi dài (VD: "abc123def456...")

⚠️ **QUAN TRỌNG**: Không chia sẻ thông tin này với ai!

## 📝 Cấu Hình

### Cách 1: Sử dụng .env file (Khuyên dùng)

Mở file `.env` và thêm:

```bash
# Telegram API credentials
TELEGRAM_API_ID=your_api_id_here
TELEGRAM_API_HASH=your_api_hash_here
TELEGRAM_PHONE=+84xxxxxxxxx  # Số điện thoại (bắt đầu với +)
TELEGRAM_SESSION_NAME=video_downloader
```

### Cách 2: Environment Variables

```bash
export TELEGRAM_API_ID=your_api_id
export TELEGRAM_API_HASH=your_api_hash
export TELEGRAM_PHONE=+84xxxxxxxxx
```

## 🚀 Sử dụng

### Lần Đầu Tiên

Lần đầu chạy, bạn sẽ được yêu cầu:

1. **Phone code**: Nhập mã từ Telegram app
2. **2FA password** (nếu bật): Nhập password

Sau đó, session sẽ được lưu vào file `video_downloader.session`

### Download Video từ Telegram

```bash
# Public channel
python cli_downloader.py "https://t.me/channel_name/123"

# Private channel (cần là member)
python cli_downloader.py "https://t.me/c/1234567890/123"
```

## 🔧 Troubleshooting

### Error: "API_ID_INVALID"
- Kiểm tra lại `TELEGRAM_API_ID` trong .env
- Đảm bảo là số, không có dấu ngoặc kép

### Error: "PHONE_NUMBER_INVALID"
- Số điện thoại phải có mã quốc gia: `+84...`
- Không có khoảng trắng hoặc dấu gạch ngang

### Error: "SESSION_PASSWORD_NEEDED"
- Account của bạn đã bật 2FA
- Nhập password 2FA khi được yêu cầu

### Error: "CHANNEL_PRIVATE"
- Bạn chưa là member của channel
- Join channel trước, sau đó thử lại

### Xóa Session và Đăng Nhập Lại

```bash
rm video_downloader.session
python cli_downloader.py "telegram_url"
```

## 📚 Telegram URL Formats

### Public Channel
```
https://t.me/channel_name/message_id
```

### Private Channel
```
https://t.me/c/channel_id/message_id
```

### Channel với Username
```
https://t.me/joinchat/invite_link
```

## 🔐 Bảo Mật

⚠️ **KHÔNG commit các file sau lên Git:**
- `.env` (đã được gitignore)
- `*.session` files (đã được gitignore)

✅ **An toàn:**
- API credentials chỉ dùng để xác thực với Telegram
- Session file được mã hóa
- Không lưu password

## 🆘 Support

Nếu gặp vấn đề:
1. Check lại credentials trong .env
2. Đảm bảo đã cài Telethon: `pip install telethon`
3. Xem logs để biết lỗi chi tiết: `--verbose`

## 📖 Thêm Thông Tin

- [Telethon Documentation](https://docs.telethon.dev/)
- [Telegram API Documentation](https://core.telegram.org/api)

---

Made with ❤️ by trancn-dev
