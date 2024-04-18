import socket
import threading


def handle_client(client_socket, addr):
    print(f"Accepted connection from {addr}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        broadcast(data)

    print(f"Connection to {addr} closed")
    client_socket.close()


def broadcast(message):
    for client in clients:
        client.sendall(message)


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 42069))
    server_socket.listen(5)

    print("Server started. Listening on port 42069")

    while True:
        client_socket, addr = server_socket.accept()

        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, addr)
        )
        client_thread.start()

        clients.append(client_socket)


clients = []

if __name__ == "__main__":
    main()
