import json
import sys
from sense_hat import SenseHat
from time import sleep
from application import Application


class EmojiDisplay(Application):
    def __init__(self, file_name=None):
        self.__sense = SenseHat()
        self._patterns = EmojiDisplay.create_shapes() if file_name is None else JSONLoader.load_from_json(file_name)
        self._running = True

    @staticmethod
    def create_shapes():
        """
        hard coded pattern creation function, used as a fallback if json file is not specified
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

    def run(self):
        while self._running:
            for emoji in self._patterns:
                self.__sense.set_pixels(emoji)
                sleep(3)
        self.__sense.clear()

    def terminate(self):
        self._running = False


class JSONLoader:
    colour_max = 255
    colour_index = 3

    @staticmethod
    def load_from_json(file_name, sense=None):
        """
        Attempts to load patterns and colours from specified json file
        Ensures format and values inside json file are correct
            e.g. pattern values are within range of colours
        :param file_name: config.json file to load from
        :param sense: SenseHat for optional error message display
        :raise FileNotFoundError
        :return:
        """
        try:
            with open(file_name, "r") as fp:
                config = json.load(fp)
            colours = config["colours"]
            patterns = config["patterns"]
            p_min, p_max, _ = JSONLoader.get_range(patterns)
            c_min, c_max, c_len = JSONLoader.get_range(colours)
            if p_min < 0:
                raise ValueError("error in {}: patterns contain values < 0".format(file_name))
            elif p_max >= len(colours):
                raise ValueError("error in {}: patterns exceed colour range".format(file_name))
            elif c_min < 0:
                raise ValueError("error in {}: colours contain values < 0".format(file_name))
            elif c_max > JSONLoader.colour_max:
                raise ValueError("error in {}: colours exceed max value of {}".format(file_name, JSONLoader.colour_max))
            elif c_len > JSONLoader.colour_index:
                raise ValueError("error in {}: colours exceed max number of values {}"
                                 .format(file_name, JSONLoader.colour_index))
            else:
                coloured_patterns = [[colours[j] for j in patterns[i]] for i in range(0, len(patterns))]
        except (FileNotFoundError, KeyError, IndexError, ValueError) as e:
            if sense is not None:
                sense.show_message("Error in loading json file", scroll_speed=0.04)
            print(str(e))
            sys.exit()
        else:
            return coloured_patterns

    @staticmethod
    def get_range(arr: list):
        a_min, a_max, a_len = 0, 0, 0
        for i in range(0, len(arr)):
            a_min = min(arr[i]) if a_min > min(arr[i]) else a_min
            a_max = max(arr[i]) if a_max < max(arr[i]) else a_max
            a_len = len(arr[i]) if a_len < len(arr[i]) else a_len
        return a_min, a_max, a_len
