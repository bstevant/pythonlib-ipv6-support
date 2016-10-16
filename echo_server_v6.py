# Echo server program
import socket

HOST = None               # None means all available interfaces
PORT = 50007              # Arbitrary non-privileged port
for af, socktype, proto, canonname, sa in socket.getaddrinfo(HOST, PORT,
        socket.AF_INET6, socket.SOCK_STREAM, 0, socket.AI_PASSIVE|socket.AI_V4MAPPED):
    try:
        with socket.socket(af, socktype, proto) as s:
            s.bind(sa)
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data: break
                    conn.sendall(data)
            break
    except socket.error as msg:
        continue
