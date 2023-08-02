import os

source = "f1.txt"
destination = "C:\\Users\\imb\\f1.txt"

try:
    if os.path.exists(destination):
        print("file already exists")
    else:
        os.replace(source,destination)
        print(source+" was moved ")
except FileNotFoundError:
    print(source +" was not found ")
