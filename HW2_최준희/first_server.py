from base64 import encode
import socket
s = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)
while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    a = 20171674
    b = str(a)
    c = b.encode()
    client.send(c)
    msg = client.recv(1024)
    print(msg.decode())
client.close()