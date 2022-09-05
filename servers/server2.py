import socket
import threading

#Create teh TCP/IP socket

sock = socket.socket(
    socket.AF_INET,  #IP_V4 Network
    socket.SOCK_STREAM #Socket obect to use IPV4
)

server_ip = '127.0.0.1' #Set the server IP
server_port = 8000 #Set the server port

server_address = (server_ip, server_port) #Set the server address

#Bind the socket to the port
sock.bind(server_address)

#Listen for incomming connections
sock.listen(10)

print("Server is running on port: ", (server_ip, server_port))

conn, client_address = sock.accept() #Accept the connection

with conn: 
    print("Connected to", client_address)

    while True:
        data = conn.recv(1024)
        print("From Connected User: ", str(data))
        # data = input(" -> ")
        message = "data received"
        # if not message:
        #     break
        conn.sendall(message.encode())
        sock.close()
        break



