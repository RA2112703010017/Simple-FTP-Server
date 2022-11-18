# Importing the required modules
import socket
import os
import time
from tkinter import filedialog
from requests import exceptions

# Creating a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((socket.gethostname(), 8888))
    s.listen(5)
    print(f"Host Name: {s.getsockname()}")

    # Accepting the connection from the client
    client, address = s.accept()

    print("socket accepted file dialog call")
    # Getting the file details of the file that is needed to be sent
    file_name = filedialog.askopenfilename(initialdir='./', title='Choose the Target File')
    print('file dialog call successfully')

    # file_size = os.path.getsize(os.path.abspath(file_name))
    file_size = os.path.getsize(file_name)

    # Sending the file details to the client
    client.send(file_name.encode())
    client.send(str(file_size).encode())

    # Opening a file stream for sending the file
    with open(file_name, 'rb') as file:
        size_sent = 0

        # Capturing the starting time
        start_time = time.time()

        # Running loop while size_sent != file_size
        while size_sent <= file_size:
            data = file.read(1024)
            if not data:
                break
            client.sendall(data)
            size_sent += len(data)

        # Capturing the Ending time
        end_time = time.time()

    print(f"File Transfer is Completed. Total Time Taken : {end_time - start_time} ")

    # Closing the socket
    s.close()

except exceptions.ConnectionError as e:
    print(e)
    s.close()
