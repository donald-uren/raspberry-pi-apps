from sense_emu import SenseHat
from time import sleep
import random

class ElectronicDie:
    x = (255, 255, 255)
    o = (0, 0, 0)
    sides = [
        [
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, x, x, o, o, o,
            o, o, o, x, x, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
        ],
        [
            o, o, o, o, o, o, o, o,
            o, o, o, x, x, o, o, o,
            o, o, o, x, x, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, x, x, o, o, o,
            o, o, o, x, x, o, o, o,
            o, o, o, o, o, o, o, o,
        ],
        [
            x, x, o, o, o, o, o, o,
            x, x, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, x, x, o, o, o,
            o, o, o, x, x, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, x, x,
            o, o, o, o, o, o, x, x,
        ],
        [
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, x, x, o, o, o,
            o, o, o, x, x, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
        ],
        [
            o, o, o, o, o, o, o, o,
            o, x, x, o, o, x, x, o,
            o, x, x, o, o, x, x, o,
            o, o, o, o, o, o, o, o,
            o, o, o, o, o, o, o, o,
            o, x, x, o, o, x, x, o,
            o, x, x, o, o, x, x, o,
            o, o, o, o, o, o, o, o,
        ],
        [
            o, o, o, o, o, o, o, o,
            o, x, x, o, o, x, x, o,
            o, x, x, o, o, x, x, o,
            o, o, o, x, x, o, o, o,
            o, o, o, x, x, o, o, o,
            o, x, x, o, o, x, x, o,
            o, x, x, o, o, x, x, o,
            o, o, o, o, o, o, o, o,
        ],
        [
            o, x, x, o, o, x, x, o,
            o, x, x, o, o, x, x, o,
            o, o, o, o, o, o, o, o,
            o, x, x, o, o, x, x, o,
            o, x, x, o, o, x, x, o,
            o, o, o, o, o, o, o, o,
            o, x, x, o, o, x, x, o,
            o, x, x, o, o, x, x, o,
        ],
    ]

    def __init__(self):
        self.__sense = SenseHat()

    def roll(self):        
        X = 0
        Y = 0
        Z = 0

        while True:
            x, y, z = self.__sense.get_accelerometer_raw().values()
            x = abs(x)
            y = abs(y)
            z = abs(z)
            
            if (x != X or y != Y or z != Z):
                for i in range(6):
                    self.__sense.set_pixels(random.choice(self.sides))
                    sleep(0.5)
                    self.__sense.clear()
                result = random.choice(self.sides)
                self.__sense.set_pixels(result)
                return self.sides.index(result) + 1
                

            X = x
            Y = y
            Z = z                

