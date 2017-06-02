import spidev
GPIO.setmode(GPIO.BCM)

class Mcp3008:
    spi = spidev.SpiDev()

    def __init__(self, bus, device, channel):
        self.__bus = bus
        self.__device = device
        self.__channel = channel

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
    def readChannel(self):
        adc = Mcp3008.spi.xfer2([1, (8 + self.__channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data


def inlezen_licht():
    lichtsensor = Mcp3008(0, 1, 0) #bus 0 dev 1 ch 0
    lichtwaarde = lichtsensor.readChannel()
    print (lichtwaarde)
    return lichtwaarde

inlezen_licht()