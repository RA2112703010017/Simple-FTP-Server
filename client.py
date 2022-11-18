# Importing the required modules
import os
import socket
import time
import requests
from tkinter import filedialog

host = input("Enter the Server's Address : ")
# host = '192.168.0.118'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Trying to connect to socket
try:
    s.connect((host, 8888))
    print("Connected Successfully")

except requests.exceptions.ConnectionError as e:
    print("Unable to Connect")
    print(e)
    exit(0)

# Receiving the file details
file_name = s.recv(100).decode()
file_size = s.recv(100).decode()

# Opening and reading file
with open(filedialog.askdirectory() + "/" + os.path.split(file_name)[1], "wb") as file:
    size_received = 0

    # Capturing the start time
    start_time = time.time()

    # Running the loop while file is received
    while size_received <= int(file_size):
        data = s.recv(1024)
        if not data:
            break
        file.write(data)
        size_received += len(data)

    # Capturing the end time
    end_time = time.time()

print(f"File Transfer is Completed. Total Time Taken : {end_time - start_time} ")

# Closing the socket
s.close()
