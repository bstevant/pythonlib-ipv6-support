# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server

res = socket.getaddrinfo(HOST, PORT, socket.AF_INET6,
                         socket.SOCK_STREAM, 0, socket.AI_V4MAPPED)
for af, socktype, proto, canonname, sa in res:
    try:
        with socket.socket(af, socktype, proto) as s:
            s.connect(sa)
            s.sendall(b'Hello, world')
            data = s.recv(1024)
            break
    except socket.error as msg:
        continue
print('Received', repr(data))
