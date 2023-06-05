import socket
import os

HTTP_OK = 'HTTP/1.1 200 OK\r\n'
ERROR_404 = 'HTTP/1.1 404 OK\r\n'
ACC = "\r\n\\Accept:text/html\r\n"
CONTENT_LENGTH = '\r\nContent-Length:'
CONTENT_IMAGE = 'Content-Type: image/jpeg'
CONTENT_JS = 'Content-Type: text/javascript;charset=utf-8'
CONTENT_CSS = 'Content-Type: text/css'
CONTENT_HTML = 'Content-Type: text/html;charset=utf-8'


def create_server(ip, port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((ip, port))
        server_socket.listen(1)
    except socket.error as msg:
        server_socket.close()
        server_socket = None
        print(msg)
    return server_socket


def read(file_path):
    co_type = content_type(file_path)
    try:
        if co_type == CONTENT_IMAGE:
            file = open(file_path, 'rb')
            content = bytearray(file.read())
            file.close()
            return co_type, content
        else:
            file = open(file_path, 'r')
            content = file.read()
            file.close()
            return co_type, content
    except:
        print('Error')


def content_type(file_path):
    arr = file_path.split('.')
    ct = arr[len(arr) - 1]
    if ct == "jpg" or ct == "gif" or ct == "JPG" or ct == "GIF":
        return CONTENT_IMAGE
    elif ct == "js":
        return CONTENT_JS
    elif ct == "html":
        return CONTENT_HTML
    elif ct == "css":
        return CONTENT_CSS
    else:
        return CONTENT_HTML


def main():
    server_socket = create_server('0.0.0.0', 5234)
    while True:
        connection, address = server_socket.accept()
        while True:
            try:
                data = connection.recv(1024).decode('utf-8')
                print(data)
                headers = data.split()
                if os.path.isfile(headers[1][1:]):
                    co_type, content = read(headers[1][1:])
                else:
                    co_type, content = read("404_ERROR.html")
                if co_type == CONTENT_IMAGE:
                    pre_con = HTTP_OK + CONTENT_IMAGE + CONTENT_LENGTH + str(len(content)) + ACC + "\r\n"
                    connection.send(pre_con.encode('utf-8') + content)
                else:
                    pre_con = HTTP_OK + co_type + CONTENT_LENGTH + str(len(content)) + ACC + "\r\n"
                    connection.send((pre_con + content).encode('utf-8'))
            except:
                print("break")
                break


if __name__ == '__main__':
    main()
