import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5014))
server_socket.listen(1)
client_socket, address = server_socket.accept()
client_socket.send(("connected".encode('utf-8')))
quitting = False
while not quitting:
    try:
        server_data = client_socket.recv(1024).decode('utf-8')
        client_socket.send(server_data.encode('utf-8'))
        print("Server recv " + server_data)
        if server_data == "Quit":
            quitting = True
            print("Disconnected")
    except:
        break
server_socket.close()
client_socket.close()
