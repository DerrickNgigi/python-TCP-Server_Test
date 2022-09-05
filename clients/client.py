import zmq

context  = zmq.Context()

# Soeket to talk to server
print("Client Started")


socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:8000")

print("Connect to the Server")
# Do 5 request and wait for response in eact time.

for request in range(5):
    print("Sending request %s ..." % request)
    socket.send_string("Hello")

    # Get the reply
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))