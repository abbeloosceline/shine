from mcpclass import MCP3008
from ledclass import LEDclass
from dbclass import DbClass
import time
import datetime

import sys
print(sys.executable)

import os
print(os.getcwd())

print(sys.path)
time.sleep(15)

leds = LEDclass(13, 19, 26)
data = DbClass()
input = MCP3008(0,0)

why = input.readLight()
left = input.readLeftButton()
right = input.readRightButton()
print(why, left, right)

def datetimefromtime(timer):
    uren = int(timer[0:2])
    minuten = int(timer[3:5])
    result = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, uren, minuten, 0)
    return result

while True:
    checker = data.getAlarmToday()
    print(checker)

    sunrise = checker[(len(checker)-6)]
    timer = checker[len(checker)-2]
    timer = datetimefromtime(timer)
    if sunrise == 1 and timer == (datetime.datetime.now() - datetime.timedelta(minutes=4)):
        print(sunrise)
        if input.readLight() == False:
            leds.sunrise()

    time.sleep(2)