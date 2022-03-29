import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
msg1 = sock.recv(1024)
print(msg1.decode())
a = 'JunHee Choi'
b = str(a)
c = b.encode()
sock.send(c)
sock.close()