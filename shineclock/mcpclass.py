from RPi import GPIO
import time

class MCP3008:
    import spidev
    GPIO.setmode(GPIO.BCM)
    spi = spidev.SpiDev()

    def __init__(self, bus, device):
        self.__bus = bus
        self.__device = device
        MCP3008.spi.open(bus, device)


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
    def readChannelValue(self, channel):
        adc = MCP3008.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

    def readLight(self):
        value = self.readChannelValue(0)
        if value > 600:
            return True
        else:
            return False

    def readLeftButton(self):
        value = self.readChannelValue(1)
        if value > 600:
            return True
        else:
            return False

    def readRightButton(self):
        value = self.readChannelValue(2)
        if value > 600:
            return True
        else:
            return False
