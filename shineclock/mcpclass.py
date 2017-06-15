from RPi import GPIO
import time

class Mcp3008:
    import spidev
    GPIO.setmode(GPIO.BCM)
    spi = spidev.SpiDev()

    def __init__(self, bus, device):
        self.__bus = bus
        self.__device = device
        Mcp3008.spi.open(bus, device)

    @property
    def bus(self):
        return self.__bus

    @property
    def device(self):
        return self.__device

    @property
    def channel(self):
        return self.__channel

    #inlezen van die kanaal (moet int tss 0-7 zijn)
    def readChannel(self, channel):
        adc = Mcp3008.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

hey = Mcp3008(0,0)
who = hey.readChannel(0)
print(who)