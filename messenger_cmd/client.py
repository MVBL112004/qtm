import socket

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 12345))
        s.sendall(f"{input('Nhap so thu nhat: ')},{input('Nhap so thu hai: ')}".encode())
        print(f"Server response: {s.recv(1024).decode()}")

if __name__ == "__main__":
    start_client()
