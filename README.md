# Multithreading-Socket-Programming
- File Server Using TCP Sockets using python language. 
- Multiple Clients Can Connect to the Server.
  - There are 3 files named file_transfer_client.py, file_transfer_client.py and file_transfer_client.py
  - First run the file_transfer_multithreaded_server.py or file_transfer_simple_server.py, then run all the above files
- Server create one thread for each client.
  - The line below will create thread for every client connection
    - `threading.Thread(target = self.listenToClient,args = (c,addr)).start()`
- File is divided into 1KB blocks and File is transferred block by block.
  - `block_size = 1024` this line in code ensures that file is recieved at the other end in 1024bytes only at a time, but you can make changes as you want.
