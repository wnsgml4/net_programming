from socket import *
from collections import defaultdict

port = 2018
BUFFSIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

dic = defaultdict(list)

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    data = data.decode()
    
    check = data.split(' ') # data의 0번째는 send, receive 확인. 1번째는 dic의 key값 확인.
    print(data)
    if check[0] == 'send':
        msg = ' '.join(check[2:])
        dic[check[1]].append(msg)
        print(dic)
        sock.sendto("OK".encode(), addr)
    elif check[0] == 'receive':
        print(dic)
        if check[1] in dic:
            if not dic[check[1]]:
                print("not")
                sock.sendto("No message".encode(), addr)
            else:
                mail = dic[check[1]].pop(0)
                print(dic)
                sock.sendto(mail.encode(), addr)
        else:
            sock.sendto("No message".encode(), addr)
    if data == 'quit':
        break