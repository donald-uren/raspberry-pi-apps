from typing import List
from sense_hat import SenseHat
from time import sleep


def shapes():
    olive = (0, 143, 0)
    pale = (255, 252, 121)
    l_blue = (4, 51, 255)
    d_blue = (1, 25, 147)
    red = (255, 38, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    patterns = [
        [
            olive, olive, olive, olive, olive, olive, olive, olive,
            olive, pale, olive, olive, pale, olive, pale, pale,
            pale, pale, l_blue, pale, pale, l_blue, pale, pale,
            pale, pale, d_blue, pale, pale, d_blue, pale, pale,
            pale, pale, pale, pale, pale, pale, pale, pale,
            pale, red, red, red, red, red, red, pale,
            pale, red, black, white, white, black, red, pale,
            pale, pale, red, red, red, red, pale, pale
        ],
        [
            olive, olive, olive, olive, olive, olive, olive, olive,
            olive, olive, olive, olive, olive, olive, olive, olive,
            pale, pale, d_blue, l_blue, pale, d_blue, l_blue, pale,
            pale, pale, white, white, pale, white, white, pale,
            pale, red, red, red, pale, pale, pale, pale,
            pale, red, black, red, pale, pale, pale, pale,
            pale, red, red, red, pale, pale, pale, pale,
            pale, pale, pale, pale, pale, pale, pale, pale
        ],
        [
            olive, olive, olive, olive, olive, olive, olive, olive,
            olive, olive, pale, pale, olive, pale, olive, olive,
            olive, l_blue, d_blue, pale, l_blue, d_blue, pale, olive,
            pale, white, white, pale, white, white, pale, pale,
            pale, pale, pale, pale, pale, pale, pale, pale,
            pale, pale, red, red, red, red, pale, pale,
            pale, red, black, white, white, black, red, pale,
            pale, red, red, red, red, red, red, pale
        ]
    ]
    return patterns


class EmojiDisplay:
    def __init__(self):
        self.__sense = SenseHat()

    def display_emoji(self):
        for emoji in shapes():
            self.__sense.set_pixels(emoji)
            sleep(3)
        self.__sense.clear()

    def stop_display(self):
        self.__sense.clear()


#
# [[79,143,0],[79,143,0],[79,143,0],[79,143,0],[79,143,0],[79,143,0],[79,143,0],[79,143,0],
#  [79,143,0],[79,143,0],[79,143,0],[79,143,0],[79,143,0],[79,143,0],[79,143,0],[79,143,0],
#  [255,252,121],[255,252,121],[1,25,147],[4,51,255],[255,252,121],[1,25,147],[4,51,255],[255,252,121],
#  [255,252,121],[255,252,121],[255,252,121],[255,252,121],[255,252,121],[255,252,121],[255,252,121],[255,252,121],
#  [255,252,121],[255,38,0],[255,38,0],[255,38,0],[255,252,121],[255,252,121],[255,252,121],[255,252,121],
#  [255,252,121],[255,38,0],[0,0,0],[255,38,0],[255,252,121],[255,252,121],[255,252,121],[255,252,121],
#  [255,252,121],[255,38,0],[255,38,0],[255,38,0],[255,252,121],[255,252,121],[255,252,121],[255,252,121],
#  [255,252,121],[255,252,121],[255,252,121],[255,252,121],[255,252,121],[255,252,121],[255,252,121],[255,252,121]]
#
# [[79,143,0],[79,143,0],[79,143,0],[79,143,0],[79,143,0],[79,143,0],[79,143,0],[79,143,0],
#  [79,143,0],[79,143,0],[255,252,121],[255,252,121],[79,143,0],[255,252,121],[79,143,0],[79,143,0],
#  [79,143,0],[4,51,255],[1,25,147],[255,252,121],[4,51,255],[1,25,147],[255,252,121],[79,143,0],
#  [255,252,121],[255,255,255],[255,255,255],[255,252,121],[255,255,255],[255,255,255],[255,252,121],[255,252,121],
#  [255,252,121],[255,252,121],[255,252,121],[255,252,121],[255,252,121],[255,252,121],[255,252,121],[255,252,121],
#  [255,252,121],[255,252,121],[255,38,0],[255,38,0],[255,38,0],[255,38,0],[255,252,121],[255,252,121],
#  [255,252,121],[255,38,0],[0,0,0],[255,255,255],[255,255,255],[0,0,0],[255,38,0],[255,252,121],
#  [255,252,121],[255,38,0],[255,38,0],[255,38,0],[255,38,0],[255,38,0],[255,38,0],[255,252,121]]

test = EmojiDisplay()
test.display_emoji()
