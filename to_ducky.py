import sys
import os


print("DELAY 150")
print("DEFAULT_DELAY 1")

for i in range(1, len(sys.argv)):
    file_name = sys.argv[i]
    try:
        file = open(file_name, "r") 
    except:
        print("Could not open file: "+file_name)
        os._exit(1)
    
    if i == 1:
        print("STRING cat > intruder")
        print("ENTER")

    for line in file:
        if not line.strip() or line.strip()[0] == "#":
            continue
        if len(line.strip()) > 2 and line.strip()[0:2] == "~~":
            print(line.rstrip('\n')[2:])
        else:
            print("STRING "+line.rstrip("\n"))
    file.close()
    
    if i == 1:
        print("CONTROL d")


