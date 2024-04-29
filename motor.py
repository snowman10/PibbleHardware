import RPi.GPIO as GPIO
from time import sleep
import digitalio, board

def initPin(pin):
    pin_gpio = digitalio.DigitalInOut(pin)
    pin_gpio.direction = digitalio.Direction.OUTPUT
    pin_gpio.value = False
    return pin_gpio

def setPinHigh(index):
    global pins
    pins[index].value = True
    sleep(1)

def setPinLow(index):
    global pins
    pins[index].value = False
    sleep(1)

def stop():
    setPinLow(0)
    setPinLow(1)

def forward():
    setPinLow(0)
    setPinHigh(1)

def reverse():
    setPinHigh(0)
    setPinLow(1)

pins = [
    initPin(board.D20),
    initPin(board.D21),
    initPin(board.D16)
]

setPinHigh(2)
forward()
stop()
reverse()
stop()