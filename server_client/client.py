import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('127.0.0.1', 5014))
connection = my_socket.recv(1024).decode('utf-8')
print(connection)
quitting = False
while not quitting:
    try:
        message = input("Enter: ")
        my_socket.send(message.encode('utf-8'))
        data = my_socket.recv(1024).decode('utf-8')
        if message == "Quit":
            quitting = True
            print("Disconnected")
        else:
            print(data)
    except:
        my_socket.close()
