from mcpclass import Mcp3008


def readLight():
    lightSensor = Mcp3008(0, 1, 0) #bus 0 dev 1 ch 0
    lightValue = lightSensor.readChannel()
    print (lightValue)
    return lightValue