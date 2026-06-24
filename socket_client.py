import socket
#socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host='127.0.0.1'
port=9001

#connect
s.connect((host,port))
# We are now connected to the server, we can send and receive data 

#now we have to decide who is sending and who is receiving, for this example we will make the server sent data
data=s.recv(1024).decode()
print("Received from server:", data)
s.close()#close the connection with the server


