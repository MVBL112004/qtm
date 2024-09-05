import requests
from bs4 import BeautifulSoup

response = requests.get('https://vnexpress.net/thu-chu-tich-nuoc-tong-bi-thu-to-lam-gui-nganh-giao-duc-khai-giang-nam-hoc-moi-4789013.html')
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    date_tag = soup.find('span', class_='date')
    if date_tag:
        date = date_tag.get_text(strip=True)
        print(f"Ngày đăng bài: {date}")
    else:
        print("Không tìm thấy thông tin ngày đăng trên trang web.")
else:
    print(f"Không thể kết nối đến trang web (HTTP status code: {response.status_code}).")