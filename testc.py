import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host='127.0.0.1'
port=8001

s.bind((host,port))

s.listen()

test, addr = s.accept()

print("Connected by", addr)

test.close()

