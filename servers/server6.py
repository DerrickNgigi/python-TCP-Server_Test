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
    from threading import Thread
    NWORKERS = 1
    TCPServer.allow_reuse_address = True
    server = TCPServer(('', 8000), EchoHandler)
    for n in range(NWORKERS):
        worker = Thread(target=server.serve_forever)
        worker.setDaemon(True)
        worker.start()
    server.serve_forever()