# file operation with x mode and os mode...

with open("calculator1234.txt","x") as file1:
    file1.write("Hello! This is Python Community!")

file1.close()

import os

if os.path.exists("calculator1234.txt"):
    os.remove("calculator1234.txt")
else:
    print("File doesn't exist!")

os.rmdir("folder")