import socket

#socket
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port=9001
#bind
s.bind((host,port))
#listen
s.listen()
#accept
client, addr = s.accept()#the variable client becomes a socket object representing the connection to that specific client.
#addr is simply information about who connected. eg: addr = ('127.0.0.1', 52341)
print("Connected by", addr)
#now we have to decide who is sending and who is receiving, for this example we will make the server sent data
data = "Hello from the server!, this is a test message"
client.sendall(data.encode())
client.close()#close the connection to the client, we can also close the server socket if we are done with it, but in this example we will keep it open to accept more clients
print(f'\n connection from {addr} closed')