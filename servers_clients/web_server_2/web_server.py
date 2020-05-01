import socket
import subprocess

'''
Простой web-сервер. Адрес: http://localhost:8000
Чтоб получить текст ответа для клиента, запускаем отдельный скрипт.
'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8000))
s.listen(1)

try:
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        with subprocess.Popen(["python3", "script.py"], stdout=subprocess.PIPE) as p:
            content, err = p.communicate()

        response = '''HTTP/1.1 200 OK
Content-Type: text/html

'''.encode() + content

        conn.send(response)
        conn.close()

except KeyboardInterrupt:
    pass
finally:
    s.close()

