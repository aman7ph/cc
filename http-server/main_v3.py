import socket

# Respond with body


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

    echo_str = "".join(path.split("/")[-1:])

    if method == "GET" and path.startswith("/echo/"):
        response = (
            "HTTP/1.1 200 OK\r\n"
            f"Content-Length: {len(echo_str)}\r\n"
            "Content-Type: text/plain\r\n"
            "\r\n"
            f"{echo_str}"
        )
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n"

    print(f"Response: {response.encode('utf-8')}")
    client_socket.send(response.encode("utf-8"))

    client_socket.close()


if __name__ == "__main__":
    main()
