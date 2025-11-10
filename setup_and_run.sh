#!/bin/bash

# =============================
# Night Checker Auto Setup Script
# =============================

echo "🌙 Starting Night Checker setup..."
echo ""

# Bước 1: Kiểm tra Python3
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 chưa được cài. Vui lòng cài đặt trước khi tiếp tục."
    exit 1
fi

# Bước 2: Tạo virtual environment nếu chưa có
if [ ! -d "venv" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment đã tồn tại, bỏ qua bước này."
fi

# Bước 3: Kích hoạt venv
echo "⚙️  Activating environment..."
source venv/bin/activate

# Bước 4: Cài đặt dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Bước 5: Chạy chương trình chính
echo ""
echo "🚀 Running Night Checker..."
python main.py

# Bước 6: Thông báo hoàn tất
echo ""
echo "✅ Hoàn tất! Kết quả đã được tạo. Cảm ơn bạn đã sử dụng Night Checker."
