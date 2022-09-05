#Server Trial Number 3

import socket

#create socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Ensure that you can restart your server quickly when it terminates

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Set the client port and server
server_ip = '127.0.0.1' #Set the server IP
server_port = 8000 #Set the server port

server_address = (server_ip, server_port) #Set the server address

#Bind the socket to the port
sock.bind(server_address)
print("Server online on:", server_address)
#Listen for incomming connections
sock.listen(10)

# loop waiting for connection (terminate with Ctrl + C)

try:
    while True:
        conn, client_address = sock.accept() #Accept the connection
        print("Connected to", client_address)

        #Looping to server a new client

        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("From Connected User: ", data)
            message  = "data received"
            conn.send(message.encode())
            sock.close()
            print("Disconnected from", client_address )

finally:
    sock.close()