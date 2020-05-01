import socket

'''
В ответ на запрос web-сервер возвращает пользователю изображение.
Запрос выполняется через браузер, адрес: http://localhost:8000
'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8000))
s.listen(1)

try:
    while True:
        conn, addr = s.accept()

        f = open("rocket.jpg", "rb")
        content = f.read()
        f.close()

        response = '''HTTP/1.1 200 OK
Content-Type: image/jpeg

'''.encode() + content

        conn.send(response)
        conn.close()

except KeyboardInterrupt:
    pass
finally:
    s.close()
