import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
block_size = 1024           #file is divided into 1kb size

s.connect((host, port))
f = open('eye.png','rb')
print('Sending...')
l = f.read(block_size)
while (l):
    print('Sending...')
    s.send(l)
    l = f.read(block_size)
f.close()
print("Done Sending")
s.shutdown(socket.SHUT_WR)
print(s.recv(1024))
s.close                     # Close the socket when done
