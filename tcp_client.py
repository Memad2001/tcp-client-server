# import socker module 
import socket

#create socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#ip or host and port 
host =socket.gethostname()
port = 555

#connect to the server
client.connect((host,port)) #ip of the server 

#receving the data 
message = client.recv(1024)

client.close()

print(message.decode("ascii"))