import socket

# Extract URL path


def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221))

    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")

    request = client_socket.recv(1024).decode("utf-8")
    print(f"Received request: {request}")

    request_line = request.split("\r\n")[0]
    print(f"Request line: {request_line}")
    method, path, _ = request_line.split(" ")
    print(f"Method: {method}, Path: {path}")

    if method == "GET" and path == "/":
        response = "HTTP/1.1 200 OK\r\n\r\n"
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n"

    print(f"Response: {response.encode('utf-8')}")
    client_socket.send(response.encode("utf-8"))

    client_socket.close()


if __name__ == "__main__":
    main()
