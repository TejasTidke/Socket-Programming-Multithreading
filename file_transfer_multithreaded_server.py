import socket
import threading

class ThreadedServer():
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 12345
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))

    def listen(self):
        self.s.listen(5)
        while True:
            c, addr = self.s.accept()
            c.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (c,addr)).start()

    def listenToClient(self, client, address):
        block_size = 1024
        print('Got connection from', address)
        print("Receiving...")
        l = client.recv(block_size)
        while (l):
            print("Receiving...")
            l = client.recv(block_size)
        print("Done Receiving")
        mssg = 'Thank You For Connecting'
        client.send(mssg.encode())
        client.close()
        
                 
if __name__ == "__main__":
    ThreadedServer().listen()
