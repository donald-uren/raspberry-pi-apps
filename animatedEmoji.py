import json
import sys
from sense_hat import SenseHat
from time import sleep


class EmojiDisplay:
    def __init__(self, file_name=None):
        self.__sense = SenseHat()
        self._patterns = EmojiDisplay.create_shapes() if file_name is None else JSONLoader.load_from_json(file_name)

    @staticmethod
    def create_shapes():
        """
        hard coded pattern creation function
        can specify a file path for config.json
        :return:
        """
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

    def display_emoji(self):
        for emoji in self._patterns:
            self.__sense.set_pixels(emoji)
            sleep(3)
        self.__sense.clear()


class JSONLoader:
    @staticmethod
    def load_from_json(file_name):
        try:
            with open(file_name, "r") as fp:
                config = json.load(fp)
            colours = config["colours"]
            patterns = config["patterns"]
            coloured_patterns = [[colours[j] for j in patterns[i]] for i in range(0, len(patterns))]
        except FileNotFoundError or KeyError or IndexError or ValueError as e:
            print(str(e))
            sys.exit()
        else:
            return coloured_patterns
