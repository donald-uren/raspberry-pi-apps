from typing import List
from sense_hat import SenseHat
from time import sleep


class EmojiDisplay:
    def __init__(self):
        self.__emojis = []
        self.__sense = SenseHat()

    def append_emoji(self, emoji: List):
        self.__emojis.append(emoji)

    def display_emoji(self):
        for emoji in self.__emojis:
            self.__sense.set_image(emoji)
            sleep(3)


def clown():
    olive = (0, 143, 0)
    pale = (255, 252, 121)
    l_blue = (4, 51, 255)
    d_blue = (1, 25, 147)
    red = (255, 38, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    pattern = [
        olive, olive, olive, olive, olive, olive, olive, olive,
        olive, pale, olive, olive, pale, olive, pale, pale,
        pale, pale, l_blue, pale, pale, l_blue, pale, pale,
        pale, pale, d_blue, pale, pale, d_blue, pale, pale,
        pale, pale, pale, pale, pale, pale, pale, pale,
        pale, red, red, red, red, red, red, pale,
        pale, red, black, white, white, black, red, pale,
        pale, pale, red, red, red, red, pale, pale
    ]
    return pattern


test = EmojiDisplay()
test.append_emoji(clown())
test.display_emoji()
