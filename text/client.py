import requests
import socket
from bs4 import BeautifulSoup

def get_word_definitions(word):
    url = f'https://www.dictionary.com/browse/{word}'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        definitions = []
        
        # Tìm tất cả các thẻ <h2>
        for h2 in soup.find_all('h2'):
            # Tìm thẻ <ol> sau thẻ <h2>
            ol = h2.find_next('ol')
            if ol:
                # Lấy tất cả văn bản trong thẻ <ol>
                list_items = ol.find_all('li')
                for li in list_items:
                    definitions.append(f"{h2.get_text(strip=True)}: {li.get_text(strip=True)}")

        # Kiểm tra và trả về các định nghĩa
        if definitions:
            return "\n".join(definitions)
        else:
            return 'Definition not found'
    except Exception as e:
        return f'Error fetching definition: {e}'

def main():
    server_address = ('localhost', 65432)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect(server_address)
            
            while True:
                word = input("Nhập từ tiếng Anh (hoặc nhập 'q' để thoát): ")
                if word.lower() == 'q':
                    sock.sendall(word.encode())  # Gửi 'q' đến server
                    print("Thoát chương trình.")
                    break

                sock.sendall(word.encode())  # Gửi từ đến server
                response = sock.recv(1024).decode()  # Nhận phản hồi từ server
                print('Received from server:', response)

                definitions = get_word_definitions(word)  # Lấy định nghĩa từ trang web
                sock.sendall(definitions.encode())  # Gửi định nghĩa đến server
                
                # Nhận phản hồi từ server
                response = sock.recv(4096).decode()
                print('Received from server:', response)

        except ConnectionResetError as e:
            print(f'Connection was reset: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
