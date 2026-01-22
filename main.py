
import os
from random import randint
from time import sleep

import receive_data


PORT = 8080

#Initialise HTTP server
def start_server():
    os.system("start cmd /c python3 server_handler.py")

start_server()

counter = 0
while True:
    counter += 1
    sleep(1)
    receive_data.data_handler()

    if counter > 100:
        break

        
    




