import socket
from Crypto.Hash import SHA256

s = socket.socket()
host = socket.gethostname()
port = 8080               
s.bind((host, port))

s.listen(1)
try:
    while True:
        c, addr = s.accept()
        print("Got connection from", addr)
        pwd = c.recv(1024)
        hash = SHA256.new()
        hash.update(pwd)
        file = open("server_passwords.txt", "r")
        currSavedPwd = file.readline()
        file.close()
        if hash.hexdigest() == currSavedPwd:
             print("Successfully logged in.")
             c.send("Successfully logged in.".encode())
             file = open("server_passwords.txt", "wb")
             file.write(pwd)
             file.close()
        else:
             print("Invalid password.")
             c.send("Invalid password.".encode())
        c.close()
except KeyboardInterrupt:
    print("Exiting.")