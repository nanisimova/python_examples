import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(input("Input command (shutdown|time|sms):").encode(), ('localhost', 8000))

mess, addr = s.recvfrom(1024)
print(mess.decode())

s.close()
