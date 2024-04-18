import os
import socket
import threading


def receive_message(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(data.decode())
        except Exception as e:
            print(f"Exception! {e}")
            break


def main():
    username = os.popen("whoami").read().rstrip("\n")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = "localhost"
    server_port = 42069
    client_socket.connect((server_address, server_port))

    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        client_socket.sendall(f"{username}: {message}".encode())


if __name__ == "__main__":
    main()
