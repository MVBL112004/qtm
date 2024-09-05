import requests
from bs4 import BeautifulSoup
response = requests.get('https://vnexpress.net/23-trieu-hoc-sinh-khai-giang-nam-hoc-moi-4788964.html')

if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')
    article_tag = soup.find('article')
    if article_tag:
        print(article_tag.get_text())
    else:
        print("No <article> tag found.")
else:
    print(f"Failed: {response.status_code} ")