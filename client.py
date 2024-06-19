import socket

s = socket.socket()
host = socket.gethostname()
port = 8080


pwd = input("Password: ").encode()

s.connect((host, port))
s.send(pwd)
print(s.recv(1024).decode())
s.close()