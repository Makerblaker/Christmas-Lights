import socket
import datetime

todayMonth = datetime.date.today().month
todayDay = datetime.date.today().day

if todayMonth == 11:
    if todayDay >= 12:
        startLights()
elif todayMonth == 12:
    startLights()
elif todayMonth == 1:
    if todayDay == 1:
        startLights()


def startLights():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 5000
    s.connect(('localhost', port))
    sendString = "PROGRAM:ON"
    s.send(sendString.encode('ascii'))
    s.close()
    print("The lights are on")
