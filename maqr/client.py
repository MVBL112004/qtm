import requests
from PIL import Image
from io import BytesIO

# URL của server
server_url = "http://127.0.0.1:5000/generate_qr"

# Chuỗi cần tạo mã QR
text_to_convert = input("Nhập chuỗi hoặc URL để tạo mã QR: ")

# Gửi yêu cầu đến Server
response = requests.post(server_url, json={"text": text_to_convert})

if response.status_code == 200:
    # Nhận ảnh mã QR và hiển thị
    qr_image = Image.open(BytesIO(response.content))
    qr_image.show()
else:
    print("Lỗi:", response.json().get("error"))
