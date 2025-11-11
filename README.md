# 🌙 NIGHT CHECKER
**Kiểm tra ví số lượng lớn qua cổng API chính thức của Midnight**
Dự án hỗ trợ cả **Windows** và **macOS/Linux**.

---

## 🚀 Tải bản mới nhất

👉 Version For MacOS: [Download NightChecker and Extract](https://github.com/DUALCORE-VuNam/night_checker/archive/refs/heads/main.zip)

> Bao gồm:
> - `NightChecker_macOS` (file chạy)
> - `addresses.txt` (file chứa danh sách ví)


Giải nén ra thư mục, bạn sẽ có cấu trúc như sau:
```
night_checker/
├── main.py
├── requirements.txt
├── setup_and_run
└── README.md
```

---

## 🪟 HƯỚNG DẪN CHO WINDOWS

### 1. Cài Python
- Tải Python từ: [https://www.python.org/downloads](https://www.python.org/downloads)
- Khi cài đặt nhớ tick chọn **“Add Python to PATH”**

### 2. Giải nén và mở thư mục dự án
- Giải nén `night_checker-main.zip` và mở bằng **Command Prompt (cmd)** tại thư mục đó.
- Cập nhật tất cả địa chỉ ví cần check vào file `addresses.txt` (Mỗi địa chỉ một dòng).

### 3. Chạy lệnh sau:
```
setup_and_run
```
Nếu gặp lỗi **Execution Policy**, mở PowerShell bằng quyền **Administrator**, sau đó chạy:
```
Set-ExecutionPolicy Unrestricted
```
Sau khi chạy, script sẽ:
- Kiểm tra và cài đặt môi trường ảo `venv`
- Cài các gói cần thiết trong `requirements.txt`
- Tự động chạy `main.py`

---

## 🍏 HƯỚNG DẪN CHO MACOS / LINUX

### 1. Cài Python
- Mặc định macOS/Linux đã có sẵn Python 3, kiểm tra bằng:
```
python3 --version
```
### 2. Cập nhật tất cả các địa chỉ ví cần check
Cập nhật tất cả địa chỉ ví cần check vào file `addresses.txt` (Mỗi địa chỉ một dòng).

### 3. Mở Terminal tại thư mục giải nén
Chạy lệnh:
```
cd path/to/night_checker-main
```
Thay "path/to" bằng đường dẫn thực tế trên máy bạn

Chạy lệnh:
```
chmod +x setup_and_run
./setup_and_run
```
Script sẽ:
- Kiểm tra và tạo môi trường ảo `venv`
- Cài đặt phụ thuộc cần thiết
- Tự động chạy chương trình

---

## ⚙️ CÁC TỆP QUAN TRỌNG
| Tệp | Mô tả |
|------|--------|
| `main.py` | Mã chính của chương trình |
| `setup_and_run` | Script tự động setup và chạy |
| `requirements.txt` | Danh sách các thư viện cần thiết |
| `README.md` | Tài liệu hướng dẫn sử dụng |

---

## 🔒 GIẤY PHÉP VÀ MIỄN TRỪ TRÁCH NHIỆM

Phần mềm này được phát hành theo **MIT License**.  
Người dùng **hoàn toàn chịu trách nhiệm** về mọi rủi ro hoặc thiệt hại phát sinh trong quá trình sử dụng.  
Tác giả **không chịu bất kỳ trách nhiệm pháp lý nào** đối với:
- Hư hại thiết bị
- Mất dữ liệu
- Sử dụng sai mục đích

Bằng cách sử dụng phần mềm này, bạn đồng ý với các điều khoản trên.

---

**© 2025 DUALCORE-VuNam — All rights reserved.**
