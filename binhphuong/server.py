# server.py
import socket
import threading

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode()
        n = int(data)
        s = n ** 2
        client_socket.send(str(s).encode())  # Sửa "endcode()" thành "encode()"
    except ValueError:
        client_socket.send("Lỗi: Đầu vào không hợp lệ".encode())  # Sửa "endcode()" thành "encode()"
    finally:
        client_socket.close()

def start_server(mode="tuantu"):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12347))  # Đảm bảo cổng là 12345
    server_socket.listen(5)
    print("Server đang chạy trên port: 12345")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Kết nối được chấp nhận từ {addr}")
        if mode == "tuantu":
            handle_client(client_socket)
        elif mode == "songsong":
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()

if __name__ == "__main__":
    mode = input("Nhập kiểu (tuantu/songsong): ").strip().lower()
    start_server(mode=mode)
