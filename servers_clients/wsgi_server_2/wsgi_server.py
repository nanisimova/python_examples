from wsgiref.simple_server import make_server

'''
Возвращаем список переменных окружения, в которых также будут
присутствовать специфические wsgi-переменные.
В качестве клиента используется браузер, URL http://localhost:8000
'''

def application(environ, start_response):
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    yield response_body.encode()

httpd = make_server('localhost', 8000, application)

# сервер работает до тех пор, пока не убъем процесс
httpd.serve_forever()
