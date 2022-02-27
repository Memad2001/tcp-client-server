#import socket module
from distutils.command.clean import clean
from email import message
from operator import truediv
import socket

#create a socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#create host and port
host = socket.gethostname()
port = 555       #you can put any port 

#bind a connection
server.bind((host,port))

#waiting for incomming connection 
server.listen(3)

while True:
    #client connection
    client,address = server.accept()
    print(f"We recevide a connection from {str(address)}")
    #message will seen by client
    message = f"The connection is establishe"
    #send a message to client
    client.send(message.encode("ascii"))
    #end the process
    client.close()