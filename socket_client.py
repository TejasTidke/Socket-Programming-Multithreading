"""
a client only needs the sequence socket(), connect()
"""
import socket

#s is socket instance and we passed it two parameters
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET refers to the address family ipv4
#SOCK_STREAM means connection oriented TCP protocol
#we can connect to a server using this socket

hostname = socket.gethostname()
port = 50007              
host = socket.gethostbyname(hostname)

s.connect((host, port))

st = 'Hey I\'m a client'
byt = st.encode()
s.send(byt)

print(s.recv(1024))
s.close()

