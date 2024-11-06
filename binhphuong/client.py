# client.py
import socket

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12347))  # Sửa cổng kết nối thành 12345

    n = input("Nhập số nguyên n: ").strip()
    client_socket.send(n.encode())

    result = client_socket.recv(1024).decode()
    print(f"Bình phương của {n} là: {result}")

    client_socket.close()

if __name__ == "__main__":
    client_program()
