import socket
import threading
from datetime import datetime

address = ""

# Set Relay GPIO pins
Relays = [4, 17, 27, 22, 5, 6, 13, 19]

# Set Switch GPIO pin

# Set LED GPIO pin

# Set Duration for flash
durationTime = '00:00:30'

# Are the lights on or off?
lightStatus = False

def main():
    global address
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        printLog('Connecting to {}:{}'.format(*address))
        client.connect(address)

        while True:
            data = input('Send:')
            data = data.encode()
            client.sendall(data)
            received_data = client.recv(64)
            if received_data:
                printLog('Received from server: {}'.format(received_data))
        client.close()

# Create print out (could add DB functionality later)
def printLog(addedText):

    print(": {}".format(addedText))

def destroy():
    printLog('Server closed @ {}:{}'.format(*address))

def setup():
    global address
    address = ('localhost', 5000)

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()