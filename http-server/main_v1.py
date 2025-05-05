import socket

# Respond with 200


def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221))

    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")

    request = client_socket.recv(1024)
    print(f"Received request: {request.decode('utf-8')}")

    response = "HTTP/1.1 200 OK\r\n\r\n"
    print(f"Response: {response.encode('utf-8')}")
    client_socket.send(response.encode("utf-8"))

    client_socket.close()


if __name__ == "__main__":
    main()
