from RPi import GPIO
import time
GPIO.setmode(GPIO.BCM)

class LEDclass():

    def __init__(self, r, g, b):
        self.__leds = [r, g, b]
        for led in self.__leds:
            GPIO.setup(led, GPIO.OUT)

        self.__rood = GPIO.PWM(r, 50)
        self.__groen = GPIO.PWM(g, 50)
        self.__blauw = GPIO.PWM(b, 50)


    def fadein(self, seconds, strength=1000):
        delay = seconds / strength
        self.__rood.start(0)
        self.__groen.start(0)
        self.__blauw.start(0)
        for i in range(strength):
            i = i/10
            self.__rood.ChangeDutyCycle(i)
            self.__groen.ChangeDutyCycle(i)
            self.__blauw.ChangeDutyCycle(i)
            time.sleep(delay)

    def fadeout(self, seconds, strength=1000):
        delay = seconds / strength
        self.__rood.start(strength/10)
        self.__groen.start(strength/10)
        self.__blauw.start(strength/10)
        for i in range(strength):
            i = i/10
            self.__rood.ChangeDutyCycle(strength/10-i)
            self.__groen.ChangeDutyCycle(strength/10-i)
            self.__blauw.ChangeDutyCycle(strength/10-i)
            time.sleep(delay)

    def breathing(self):
        strenghts = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 200]
        for i in strengths:
            self.fadein(7, i)
            self.fadeout(4, i)
            time.sleep(1)

    def sundown(self):
        self.fadein(3)
        self.fadeout(180)

    def sunrise(self):
        self.fadein(300)