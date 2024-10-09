import socket

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 12345))
        s.listen()
        conn, _ = s.accept()
        with conn:
            while data := conn.recv(1024).decode():
                try:
                    num1, num2 = map(float, data.split(","))
                    conn.sendall(f"{num1} + {num2} = {num1 + num2}".encode())
                except ValueError:
                    conn.sendall(b"Invalid input. Send two numbers separated by a comma.")

if __name__ == "__main__":
    start_server()
