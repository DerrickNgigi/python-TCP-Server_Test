import socket
import time

host = "127.0.0.1"
port = 8000

client_socket = socket.socket()   #instatiate
client_socket.connect((host, port))     #Connect to the server

# message = "I love doing this challenge with HTML and CSS"

try:
    count = 0
    for request in range(20):
        # while True:
        print("Sending message to the server")
        time.sleep(1)
        count += 1
        message = "I am Client Three " + str(count)
        client_socket.sendall(message.encode()) #send message
        print("Sent message to the server")

        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal

finally:
    print("Closing the socket")
    client_socket.close()
