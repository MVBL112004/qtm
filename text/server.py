import socket

def main():
    server_address = ('localhost', 65432)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(server_address)
        server_socket.listen()
        print('Waiting for a connection...')

        while True:
            connection, client_address = server_socket.accept()
            with connection:
                print('Connected by', client_address)

                while True:
                    # Nhận từ từ client
                    word = connection.recv(1024).decode()
                    if not word:  # Kiểm tra nếu client đã ngắt kết nối
                        break
                    print('Received word from client:', word)

                    if word.lower() == 'q':  # Nếu client gửi 'q', thoát vòng lặp
                        print("Client requested to close the connection.")
                        break

                    # Gửi phản hồi
                    response_message = 'Message received'
                    connection.sendall(response_message.encode())

                    # Nhận định nghĩa từ client (nếu cần)
                    definition = connection.recv(4096).decode()
                    print('Received definition from client:', definition)

                    # Gửi lại định nghĩa cho client
                    connection.sendall(definition.encode())
                
                print(f'Connection with {client_address} closed.')

if __name__ == '__main__':
    main()
