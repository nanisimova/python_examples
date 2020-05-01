import socket

'''
Простейший web-сервер, на любой запрос возвращает "Hello, world!".
Запрос выполняется в браузере, адрес http://localhost:8000
'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8000))
s.listen(1)

try:
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        content = "Hello, world!"

        response = '''HTTP/1.1 200 OK
Content-Type: text/html

'''.encode() + content.encode()

        conn.send(response)
        conn.close()

except KeyboardInterrupt:
    s.close()

