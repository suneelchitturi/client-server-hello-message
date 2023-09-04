Server message to Client

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))

s.listen(5)

full_msg = ""
while True:
    con, add = s.accept()
    print(f"connection is established via {add}")
    while True:
        data = con.recv(16)
        if not data:
            break
        full_msg += data.decode()
    print(full_msg)
    full_msg = ""
    con.send("Hello".encode())
    con.shutdown(1)


Server message to Client

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    msg = input("Hello ")
    if msg == "q":
        break
    s.send(msg.encode())
    s.shutdown(1)

    full_msg = "Hello"
    while True:
        data = s.recv(16)
        if not data:
            break
        full_msg += data.decode()
    print(full_msg)



