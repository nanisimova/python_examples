import socket
import time
import random
from queue import Queue

'''
Сервер принимает запросы разных типов:
* "time" - возвращает текущее время
* "sms" - ставит задачу в очередь и возвращает клиенту подтверждение "done".
IRL это могла бы быть любая отложенная задача, не требующая немедленного подтверждения
выполнения, отправка sms пользователю, email, или некая обработка данных.
* "shutdown" - завершает работу сервера, отображает все, что накопилось в очереди.
'''

q = Queue()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 8000))

try:
    while True:
        mess, addr = s.recvfrom(1024)
        mess = mess.decode()
        if mess == 'shutdown':
            s.sendto('done'.encode(), addr)
            break
        elif mess == 'time':
            s.sendto(time.ctime().encode(), addr)
        elif mess == 'sms':
            q.put("sms " + str(random.randint(1,10)))
            s.sendto('done'.encode(), addr)

except KeyboardInterrupt:
    pass

s.close()

while not q.empty():
    print(q.get())

