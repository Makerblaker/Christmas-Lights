import RPi.GPIO as GPIO
import socket
import threading
import time
from time import sleep
import datetime

address = ('localhost', 5000)
server = ''

# Set Relay GPIO pins
Relays = [4, 17, 27, 22]

# Set Duration for flash
durationTime = '00:00:30'

# are the lights on or off?
lightStatus = False

# Setup all the stuff we need.
def setup():
    global server
    print('Setting up Christmas light server...')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Starting up the server @ {}:{}'.format(*address))
    server.bind(address)
    server.listen(100)
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)
    
    for i in Relays:
        GPIO.setup(i, GPIO.OUT)
        relay(i, GPIO.HIGH)

def main():
    global server, lightStatus

    while True:
        clientSocket,addr = server.accept()

        fromClient = clientSocket.recv(1024)
        clientSocket.close()

        print(fromClient.decode('ascii'))
        requestType = fromClient.decode('ascii').split(':')

        if requestType[0] == "PROGRAM":
            if requestType[1] == "ON":
                lightStatus = True

                # Start flash
                t = threading.Thread(target=flash)
                t.start()
                
                relay(Relays[0], GPIO.LOW)
                print("Lights on")
            elif requestType[1] == "OFF":
                lightStatus = False
                for i in Relays:
                    relay(i, GPIO.HIGH)
                print("Lights off")

        elif requestType[0] == "RELAY":
            if requestType[2] == "ON":
               relay(Relays[int(requestType[1])], GPIO.LOW)
            else:
                relay(Relays[int(requestType[1])], GPIO.HIGH)

def flash():
    global lightStatus
    # Convert people time to seconds
    duration = time.strptime(durationTime,'%H:%M:%S')
    totalDuration = datetime.timedelta(hours=duration.tm_hour,minutes=duration.tm_min,seconds=duration.tm_sec).total_seconds()

    # Alternate relays (Red and Green on lawn)
    while lightStatus:
        relay(Relays[1], GPIO.LOW)
        sleep(totalDuration)
        relay(Relays[1], GPIO.HIGH)
        relay(Relays[2], GPIO.LOW)
        sleep(totalDuration)
        relay(Relays[2], GPIO.HIGH)
        relay(Relays[3], GPIO.LOW)
        sleep(totalDuration)
        relay(Relays[3], GPIO.HIGH)

def relay(relaySelect, onoff):
    GPIO.output(relaySelect, onoff)
    if onoff == GPIO.HIGH:
        status = "OFF"
    else:
        status = "ON"
    print("Relay {} is {}".format(relaySelect, onoff))

def destroy():
    print('Closing the server...')

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
