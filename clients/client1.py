import socket
import sys

#SET UP A TCP/IP SERVER

tcp_socket = socket.create_connection(('localhost', 8000))

try:
    data = "Let see if this client can connect to the server"
    byt=data.encode()
    tcp_socket.sendall(data)

finally:
    print("Closing the Socket")
    tcp_socket.close()