import RPi.GPIO as GPIO
import datetime
import time

time.sleep(5)

HexDigits = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f, 0x77,
             0x7c, 0x39, 0x5e, 0x79, 0x71]

ADDR_AUTO = 0x40
ADDR_FIXED = 0x44
STARTADDR = 0xC0
DISPLAYON = 0x88

class TMDisplay:

    def __init__(self, CLK, DA):
        self.__CLK = CLK
        self.__DA = DA

        self.__brightness = 0x07
        self.__doublePoint = True
        self.__setup()

    @property
    def doublePoint(self):
        return self.__doublePoint

    @doublePoint.setter
    def doublePoint(self, value):
        self.__doublePoint = value

    def __setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__CLK, GPIO.OUT)
        GPIO.setup(self.__DA, GPIO.OUT)

    def __start(self):
        GPIO.output(self.__CLK, GPIO.HIGH)
        GPIO.output(self.__DA, GPIO.HIGH)
        GPIO.output(self.__DA, GPIO.LOW)
        GPIO.output(self.__CLK, GPIO.LOW)

    def __stop(self):
        GPIO.output(self.__CLK, GPIO.LOW)
        GPIO.output(self.__DA, GPIO.LOW)
        GPIO.output(self.__CLK, GPIO.HIGH)
        GPIO.output(self.__DA, GPIO.HIGH)

    def __writeBit(self,bit):
        GPIO.output(self.__CLK, GPIO.LOW)
        GPIO.output(self.__DA, bit)
        GPIO.output(self.__CLK, GPIO.HIGH)

    def __ack(self):
        GPIO.output(self.__CLK, GPIO.LOW)
        GPIO.setup(self.__DA, GPIO.IN, GPIO.PUD_UP)    #moet na de klok laag staan? moet geen pullup zijn
        time.sleep(0.001)
        GPIO.output(self.__CLK, GPIO.HIGH)
        GPIO.setup(self.__DA, GPIO.OUT)

    def __writeByte(self,byte):
        filter = 0x01
        for i in range(0,8):
            if (byte & filter) > 0 :
                self.__writeBit(True)
            else:
                self.__writeBit(False)
            filter = filter << 1

    def writeDigits(self,data):
        self.__start()
        self.__writeByte(ADDR_AUTO)
        self.__ack()
        self.__stop()

        self.__start()
        self.__writeByte(STARTADDR)
        self.__ack()
        for i in range(0,4):
            if self.doublePoint:
                self.__writeByte(HexDigits[data[i]] | 0x80)
            else:
                self.__writeByte(HexDigits[data[i]] )
            self.__ack()

        self.__stop()
        self.__start()
        self.__writeByte((DISPLAYON | self.__brightness))
        self.__ack()
        self.__stop()

    def writeDigit(self,position, data):
        self.__start()
        self.__writeByte(ADDR_FIXED)
        self.__ack()
        self.__stop()

        self.__start()
        self.__writeByte(STARTADDR | position)
        self.__ack()
        self.__writeByte(HexDigits[data])
        self.__ack()

        self.__stop()
        self.__start()
        self.__writeByte((DISPLAYON | self.__brightness))
        self.__ack()
        self.__stop()

    def writeTime(self):
        timestring = str(datetime.datetime.now())
        timelist = [int(timestring[11]), int(timestring[12]), int(timestring[14]), int(timestring[15])]
        self.writeDigits(timelist)


hey = TMDisplay(21, 20)
while True:
    hey.writeTime()