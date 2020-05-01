from wsgiref.simple_server import make_server

'''
В качестве клиента используем браузер, URL http://localhost:8000
'''

def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    yield b'Hello world!\n'

httpd = make_server('localhost', 8000, application)
# выполняем только один запрос
httpd.handle_request()
