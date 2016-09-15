# from: https://docs.python.org/3.1/library/asyncore.html#asyncore-example-basic-echo-server
import asyncore
import socket

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192)
        self.send(data)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        #for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC,
        #                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        #    af, socktype, proto, canonname, sa = res
        #    self.create_socket(af, socktype)
        self.create_socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is None:
            return
        else:
            sock, addr = pair
            print('Incoming connection from %s' % repr(addr))
            handler = EchoHandler(sock)

# Wait in tcp46 on MacOSX
server = EchoServer('::', 8080)
# Wait in tcp6 on MacOSX
#server = EchoServer('localhost', 8080) 
asyncore.loop()