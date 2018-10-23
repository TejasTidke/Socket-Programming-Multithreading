import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
block_size = 1024           #file is divided into 1kb size

s.bind((host, port))        # Bind to the port
#f = open('paris.png','wb')
s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    print("Receiving...")
    l = c.recv(block_size)
    while (l):
        print("Receiving...")
        l = c.recv(block_size)
    #f.close()
    print("Done Receiving")
    mssg = 'Thank You For Connecting'
    c.send(mssg.encode())
    c.close()                # Close the connection
