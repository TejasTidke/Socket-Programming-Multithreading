import socket

#s is socket instance and we passed it two parameters
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET refers to the address family ipv4
#SOCK_STREAM means connection oriented TCP protocol
#we can connect to a server using this socket

#A server has a bind() method which binds it to a specific ip
#and port so that it can listen to incoming requests on that ip and port.
port = 50007
s.bind(('', port))

#A server has a listen() method which puts the server into listen mode.
"""  
socket.listen(backlog)
Listen for connections made to the socket.
The backlog argument specifies the maximum number of queued connections and should be at least 0;
the maximum value is system-dependent (usually 5), the minimum value is forced to 0.
"""
s.listen(5)

"""
#And last a server has an accept() and close() method.
#The accept method initiates a connection with the client and
#the close method closes the connection with the client. 
"""

while True:
    c, addr = s.accept()
    """
    accept return value is a pair (conn, address)
    where conn is a new socket object usable to send and receive data on the connection,
    and address is the address bound to the socket on the other end of the connection.
    """
    print('Got connection from', addr)
    
    print(c.recv(1024))
    
    st = 'Congrats, You are Connected!!'
    byt = st.encode()
    c.send(byt) 
    c.close() 
