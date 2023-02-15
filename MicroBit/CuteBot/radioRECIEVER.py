# CalciumSelenide - Wed Feb 14 06:48:15 PM CST 2022
from microbit import *
import radio

class Transciever:
    # Initialize the Controller class
    def __init__(self, messageLength: int, messageQueue: int,
                 radioChannel: int, broadcastStrength: int,
                 messageAddress: int, groupAddress: int):
        # Set all the variables for the controller class to inherit
        self.msgLength = messageLength
        self.msgQueue = messageQueue
        self.msgAddress = messageAddress
        self.grpAddress = groupAddress
        self.radioChannel = radioChannel
        self.broadcastStrength = broadcastStrength

        # Radio status
        self.status = "ON"

        # Radio message parameters
        self.message = ""
        self.rssi = None
        self.timestamp = ""

        # Turn the radio on for the initalization
        radio.on()

        # Set the radio configuration
        radio.config(length=self.msgLength, queue=self.msgQueue,
                     channel=self.radioChannel, power=self.broadcastStrength,
                     address=self.msgAddress, group=self.grpAddress)

        # Setting UART/Serial communications up
        self.serialMessage = ""

    def on(self):
        radio.on()
        self.status = "ON"

# ----------- RADIO functions of the Transciever class --------------
    def off(self):
        radio.off()
        self.status = "OFF"

    def send(self, message):
        radio.send(message)

    def recieve(self):
        tmpDetails = radio.receive_full()
        if tmpDetails:
            self.message, self.rssi, self.timestamp = tmpDetails
        else:
            self.message = ""
            self.rssi = None
            self.timestamp = ""

# ----------- UART/SERIAL functions of the Transciever class --------
    def serialEnable(self, baudRate, msgBits, msgParity, stopBits):
        uart.init(baudrate=baudRate, bits=msgBits, parity=msgParity,
                  stop=stopBits, tx=None, rx=None)

    def serialRead(self):
        serialMsg = uart.readline()
        self.serialMessage = str(serialMsg)

    def serialWrite(self, usrMessage):
        uart.write(usrMessage)

messageLength = 8  # The maximum byte length: can be up to 251 bytes
messageQueue = 1  # The amount of messages that can be stored in queue
radioChannel = 0  # Can be any value between 0 and 83
broadcastStrength = 6  # Can be any value betweeon 0 (weakest) and 7 (strongest)
messageAddress = 0x012345678  # A 32bit address    **
groupAddress = 0  # Can be any value between 0 and 255  **

# ** A messageAddress is like a house, and groupAddress is the person in that
#    that house that the message it to.
myBot = Transciever(messageLength, messageQueue, radioChannel,
                    broadcastStrength, messageAddress, groupAddress)

# while True:
    # myBot.recieve()
    # if myBot.message:
        # display.scroll(myBot.message[3:], wait=True)
