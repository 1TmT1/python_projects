import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.1.18", 5256))

image = open("screen.jpg", "wb")
while True:
    content = client_socket.recv(1024)
    if not content:
        break
    else:
        image.write(content)
