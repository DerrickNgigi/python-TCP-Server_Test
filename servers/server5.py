from socketserver import BaseRequestHandler, TCPServer, ThreadingTCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Connection Acquired', self.client_address)
        while True:
            message = self.request.recv(1024)
            if not message:
                break
            print("Received Message: ", message.decode())
            self.request.send(message)


if __name__ == '__main__':
    server = ThreadingTCPServer(('', 8000), EchoHandler)
    server.serve_forever()