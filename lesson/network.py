import socket


ip = "192.168.1.22"
port = 5725
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip, port))
server_socket.listen(1)
connection, address = server_socket.accept()


def send_client_enc(message):
    connection.send(message.encode("utf-8"))


def recv_client_dec(bytes):
    connection.recv(bytes).decode("utf-8")


def send_client(message):
    connection.send(message)


def recv_client(bytes):
    connection.recv(bytes)
