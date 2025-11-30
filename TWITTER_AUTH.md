# 🐦 Hướng Dẫn Xác Thực Twitter/X.com

## 📌 Giới Thiệu

Tool này hỗ trợ download video từ Twitter/X.com, **bao gồm video protected** (chỉ người theo dõi mới xem được). Để download được video protected, bạn cần xác thực tài khoản Twitter của mình.

## 🎯 Khi Nào Cần Xác Thực?

✅ **CẦN xác thực nếu:**
- Video từ tài khoản protected (khóa, chỉ followers mới xem)
- Video trong private tweet
- Download nhiều video liên tục (tránh rate limit)

❌ **KHÔNG CẦN xác thực nếu:**
- Video public (ai cũng xem được)
- Download thỉnh thoảng

## 🔑 Cách 1: Sử dụng Cookies (Khuyên Dùng)

### Bước 1: Cài Extension

**Chrome/Edge:**
1. Mở Chrome Web Store
2. Tìm **"Get cookies.txt LOCALLY"** (by Rahul Shaw)
3. Click "Add to Chrome"

**Firefox:**
1. Mở Firefox Add-ons
2. Tìm **"cookies.txt"**
3. Click "Add to Firefox"

🔗 Links:
- Chrome: https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc
- Firefox: https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/

### Bước 2: Đăng Nhập Twitter/X

1. Mở browser và truy cập **https://x.com**
2. **Đăng nhập** vào tài khoản Twitter của bạn
3. Đảm bảo đã "Stay signed in"

### Bước 3: Export Cookies

1. **Trên trang x.com**, click vào icon extension
2. Click **"Export"** hoặc **"Download"**
3. Lưu file với tên `cookies.txt`
4. Copy file vào thư mục project:
   ```
   Download-video/cookies.txt
   ```

### Bước 4: Cấu Hình

Không cần làm gì thêm! Tool sẽ tự động detect file `cookies.txt`

## 🔑 Cách 2: Sử dụng Auth Token (Alternative)

### Lấy Auth Token từ Browser

1. Đăng nhập vào **https://x.com**
2. Mở **DevTools** (F12)
3. Vào tab **Network**
4. Reload trang (Ctrl+R)
5. Click vào bất kỳ request nào tới `x.com`
6. Tìm header **"authorization"**
7. Copy giá trị (dạng: `Bearer AAAAAAAAAAAAAAAAAAAAAxxxxx...`)

### Cấu Hình

Mở file `.env` và thêm:
```bash
TWITTER_AUTH_TOKEN=Bearer_AAAAAAAAAxxxxxxxxx
```

## 📝 Cách Sử Dụng

### Với Cookies (Cách 1)

```bash
# Chỉ cần có file cookies.txt trong thư mục
python cli_downloader.py "https://x.com/user/status/123"
```

### Với Auth Token (Cách 2)

```bash
# Đã config trong .env
python cli_downloader.py "https://x.com/user/status/123"
```

## 🔧 Troubleshooting

### Lỗi: "Protected tweet"

**Nguyên nhân:** Bạn chưa xác thực hoặc cookies đã hết hạn

**Giải pháp:**
1. Kiểm tra file `cookies.txt` có tồn tại không
2. Export lại cookies (cookies hết hạn sau ~30 ngày)
3. Đảm bảo bạn đã follow tài khoản protected đó

### Lỗi: "Rate limit exceeded"

**Nguyên nhân:** Download quá nhiều trong thời gian ngắn

**Giải pháp:**
1. Chờ 15 phút rồi thử lại
2. Sử dụng cookies để tăng rate limit

### Lỗi: "Invalid cookies"

**Nguyên nhân:** File cookies.txt không đúng format

**Giải pháp:**
1. Đảm bảo dùng đúng extension "Get cookies.txt LOCALLY"
2. Export lại từ trang x.com (không phải twitter.com)
3. Kiểm tra file không bị corrupt

### Lỗi: "Tweet not found"

**Nguyên nhân:**
- Tweet đã bị xóa
- URL không đúng
- Bạn không có quyền xem tweet

**Giải pháp:**
1. Kiểm tra lại URL
2. Đảm bảo bạn có thể xem tweet trên browser
3. Nếu là protected account, đảm bảo bạn đã follow

## 🔒 Bảo Mật

### ⚠️ QUAN TRỌNG:

- **KHÔNG** commit file `cookies.txt` lên Git
- **KHÔNG** chia sẻ cookies với người khác
- Cookies = quyền truy cập tài khoản của bạn!

### ✅ An Toàn:

- File `cookies.txt` đã được thêm vào `.gitignore`
- Chỉ lưu cookies trên máy local
- Đổi password Twitter = cookies sẽ invalid

## 📱 Lưu Ý Cho Windows/WSL Users

Nếu bạn dùng WSL:

```bash
# Nếu cookies.txt ở Windows
cp /mnt/c/Users/YourName/Downloads/cookies.txt ~/projects/download/Download-video/

# Hoặc tạo symlink
ln -s /mnt/c/Users/YourName/Downloads/cookies.txt ~/projects/download/Download-video/cookies.txt
```

## 🎬 Download Video Protected

### Ví Dụ:

```bash
# Tweet protected từ tài khoản mà bạn follow
python cli_downloader.py "https://x.com/protected_user/status/123456789"

# Chọn chất lượng
python cli_downloader.py "https://x.com/protected_user/status/123456789" --quality

# Custom output folder
python cli_downloader.py "https://x.com/protected_user/status/123456789" -o /path/to/folder
```

## 📖 Thêm Thông Tin

### Twitter API Rate Limits:

- **Không xác thực:** 150 requests/15 phút
- **Có xác thực:** 900 requests/15 phút

### Cookie Expiration:

- Cookies thường valid trong **30 ngày**
- Nếu đổi password = cookies invalid ngay lập tức
- Auto-logout = cần export cookies mới

## ❓ FAQ

**Q: Tôi có thể dùng cookies từ nhiều tài khoản không?**
A: Có, nhưng chỉ 1 file cookies.txt tại 1 thời điểm. Đổi tên file nếu muốn switch.

**Q: Cookies có an toàn không?**
A: Chỉ an toàn nếu bạn giữ file trên máy của mình. KHÔNG share với ai.

**Q: Tôi có thể download video của người không follow mình không?**
A: Có, nếu account đó không protected.

**Q: Extension có an toàn không?**
A: "Get cookies.txt LOCALLY" export cookies LOCAL, không gửi đi đâu. Check reviews trên store.

---

Made with ❤️ by trancn-dev
