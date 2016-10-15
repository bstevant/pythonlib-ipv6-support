# Echo server program
# from: https://docs.python.org/3.1/library/socket.html

import socket
import sys

#HOST = None               # Symbolic name meaning all available interfaces, open tcp46 on IPv6-enabled host
HOST = 'localhost'
PORT = 50007              # Arbitrary non-privileged port
s = None

try:
    res = socket.getaddrinfo(HOST, PORT, socket.AF_INET6,
                             socket.SOCK_STREAM, 0, socket.AI_PASSIVE|socket.AI_V4MAPPED)
except socket.gaierror as msg:
    print('Could not resolve hostname "{}": {}'.format(HOST, msg))
    sys.exit(1)
for af, socktype, proto, canonname, sa in res:
    try:
        s = socket.socket(af, socktype, proto)
        s.bind(sa)
        break
    except socket.error as msg:
        if not s:
            print('Could not create socket: {}'.format(msg))
        else:
            print('Could not bind socket: {}'.format(msg))
            s.close()
            s = None
else:
    print('No socket could be created/bound')
    sys.exit(1)
del res

print('Bound to {}'.format(s.getsockname()))
s.listen(1)
conn, addr = s.accept()
print('Connection from {}'.format(addr))
while True:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close()
s.close()
