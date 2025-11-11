import sys
import os
import requests
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed


base_url = "https://scavenger.prod.gd.midnighttge.io/statistics/"


if getattr(sys, 'frozen', False):  
    app_path = os.path.dirname(sys.executable)
else:  
    app_path = os.path.dirname(os.path.abspath(__file__))

addresses_file = os.path.join(app_path, "addresses.txt")


if not os.path.exists(addresses_file):
    print("⚠️ Không tìm thấy file addresses.txt trong thư mục hiện tại!")
    print("👉 Hãy tạo file addresses.txt và thêm mỗi địa chỉ ví trên 1 dòng.")
    input("\nNhấn Enter để thoát...")
    sys.exit(1)

with open(addresses_file, "r", encoding="utf-8") as f:
    addresses = [line.strip() for line in f if line.strip()]

if not addresses:
    print("⚠️ File addresses.txt trống, không có địa chỉ ví nào!")
    input("\nNhấn Enter để thoát...")
    sys.exit(1)


desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_file = os.path.join(desktop_path, "Night_Allocation_Summary.csv")


def fetch_allocation(addr):
    try:
        r = requests.get(base_url + addr, timeout=10)
        r.raise_for_status()
        data = r.json()
        allocation = data.get("local", {}).get("night_allocation", 0)
        return addr, allocation
    except Exception as e:
        return addr, f"Lỗi: {e}"


results = []
total_allocation = 0.0

print(f"⏳ Đang truy vấn {len(addresses)} địa chỉ ví từ API...\n")

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(fetch_allocation, a) for a in addresses]
    for f in as_completed(futures):
        addr, value = f.result()
        results.append((addr, value))
        print(f"{addr}: {value}")
        if isinstance(value, (int, float)):
            total_allocation += value


with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Address", "Night Allocation"])
    for addr, value in results:
        writer.writerow([addr, value])
    writer.writerow([])
    writer.writerow(["TOTAL", total_allocation])

print("\n✅ Hoàn tất!")
print(f"👉 Tổng night_allocation: {total_allocation}")
print(f"📁 File kết quả đã lưu tại: {output_file}")

input("\nNhấn Enter để thoát...")
