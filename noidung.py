import requests
from bs4 import BeautifulSoup

response = requests.get('https://vnexpress.net/23-trieu-hoc-sinh-khai-giang-nam-hoc-moi-4788964.html')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    article_tag = soup.find('article')
    date_tag = soup.find('span', class_='date')
    if article_tag:
        title = soup.title.string
        title_content = title.get_text(strip=True)
        date = date_tag.get_text(strip=True)
        # Chuyển tiêu đề thành chữ in hoa
        title_content_upper = title_content.upper()
        # Thêm tiêu đề vào tệp article_content.txt
        with open('article_content.txt', 'w', encoding='utf-8') as file:
            file.write(title_content_upper + '\n')  # Ghi tiêu đề và xuống dòng
            file.write(f"Ngày đăng bài: {date}\n")  # Ngày tháng
            file.write(article_tag.get_text(strip=True)) # Nội dung
        print("Đã ghi tiêu đề vào tệp article_content.txt thành công!")
    else:
        print("Không tìm thấy thẻ <article> trên trang web.")
else:
    print(f"Không thể kết nối đến trang web (HTTP status code: {response.status_code}).")
