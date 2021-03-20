
import time
import socket
import hashlib

tcp_client = socket.socket()
ip = input("请输入完整的服务端ip：")
port = ip.split(':')[1]
print('将要连接：%s:%s' % (ip, port))
start_time = time.time()

print('正在连接····· %s ' % (time.time() - start_time))
tcp_client.connect((ip,int(port)))
print('已连接')

while True:
    command = input(">")
    tcp_client.send(command.encode())
    if command == "exit":
        break
tcp_client.close()