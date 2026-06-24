import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host= '127.0.0.1'
port=8001

s.connect((host,port))

data=s.recv(1024).decode()

print("Received from server:", data)

s.close()

