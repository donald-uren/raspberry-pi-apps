from sense_hat import SenseHat
from time import sleep
import random


# Dice object
class ElectronicDice:
    x = (255, 255, 255)
    o = (0, 0, 0)
    # Different sides of a dice
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

    # Call the dice to roll
    def roll(self):
        while True:
            acceleration = self.__sense.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']

            x = abs(x)
            y = abs(y)
            z = abs(z)

            # Check if the sense_hat is being shaked
            if 2 in (x, y, z):
                for i in range(3):
                    self.__sense.set_pixels(random.choice(self.sides))
                    sleep(0.5)
                    self.__sense.clear()
                result = random.choice(self.sides)
                print(self.sides.index(result) + 1)
                self.__sense.set_pixels(result)
                sleep(2)
                return self.sides.index(result) + 1
            else:
                self.__sense.clear()
