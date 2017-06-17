from RPi import GPIO
import time

class SegmentClass():
    delaylow = 0.00025
    delayhigh = 0.00025

    numbers = [0b00111111,
               0b00000110,
               0b01011011,
               0b01001111,
               0b01100110,
               0b01101101,
               0b01111101,
               0b00000111,
               0b01111111,
               0b01101111,
               0b00000000]

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        segments = [16, 12, 24, 23, 18, 20, 21]
        for segment in segments:
            GPIO.setup(segment, GPIO.OUT)
            GPIO.output(segment, False)
        digits = [6, 13, 19, 26]
        for digit in digits:
            GPIO.setup(digit, GPIO.OUT)
            GPIO.output(digit, True)

    def writedigit(self, digit):
        GPIO.output(digits[digit-1], False)
        time.sleep(VierxZevenSegmentDisplay.delay)
        GPIO.output(digits[digit-1], True)

    def cleardisplay(self):
        for x in segments:
            GPIO.output(x, False)

    def writesegment(self, number):
        byte = numbers[number]
        for element in segments:
            bit = byte & 1
            bit = ~bit
            GPIO.output(element, bit)
            byte >>= 1

hey = SegmentClass()
hey.writesegment(2)
while True:
    hey.writedigit(2)