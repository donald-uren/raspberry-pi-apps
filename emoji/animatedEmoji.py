import json
import sys
from typing import List
from sense_hat import SenseHat
from time import sleep
from display import AbstractDisplay


class EmojiDisplay(AbstractDisplay):
    """
    Class for housing and displaying a collection of emojis
    overrides run() from abstract class Application - refer to display.py for details
    """

    def __init__(self, file_name=None):
        super().__init__()
        self.__sense = SenseHat()
        self._patterns = EmojiDisplay.create_shapes() if file_name is None else JSONLoader.load_from_json(file_name)

    def run(self):
        """
        iterates through emoji list and displays on SenseHat (until joystick is pressed)
        overrides run() in AbstractDisplay (see display.py)
        :return: void
        """
        while self._running:
            for emoji in self._patterns:
                self.__sense.set_pixels(emoji)
                sleep(3)
        self.__sense.clear()

    @staticmethod
    def create_shapes():
        """
        hard coded pattern creation function, used as a fallback if json file is not specified
        see JSONLoader.load_from_json() for dynamic version
        :return: patterns list
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


class JSONLoader:
    """
    simple class to house json loading/parsing, and creation of a patterns list
    a patterns list is a list of lists, each containing RGB values for displaying an emoji
    """
    colour_max = 255
    colour_index = 3
    pixel_max = 64

    @staticmethod
    def load_from_json(file_name, sense=None):
        """
        Attempts to load patterns and colours from specified json file
        Ensures format and values inside json file are correct
            e.g. pattern values are within range of colours
        :param file_name: config.json file to load from
        :param sense: SenseHat for optional error message display
        :raise FileNotFoundError
        :return: void
        """
        try:
            with open(file_name, "r") as fp:
                config = json.load(fp)
            colours = config["colours"]
            patterns = config["patterns"]
            p_min, p_max, p_len = JSONLoader.get_range(patterns)
            c_min, c_max, c_len = JSONLoader.get_range(colours)
            if p_min < 0:  # patterns contain a colour list index below 0
                raise ValueError("error in {}: patterns contain values < 0".format(file_name))
            elif p_max >= len(colours):  # patterns contain index outside of colour list
                raise ValueError("error in {}: patterns exceed colour range".format(file_name))
            elif p_len > JSONLoader.pixel_max:  # patterns contain more than 64 pixels
                raise ValueError("error in {}: patterns exceeded 64 pixels".format(file_name))
            elif c_min < 0:  # colours contain RGB values below 0
                raise ValueError("error in {}: colours contain values < 0".format(file_name))
            elif c_max > JSONLoader.colour_max:  # colours contain RGB values greater than 255
                raise ValueError("error in {}: colours exceed max value of {}"
                                 .format(file_name, JSONLoader.colour_max))
            elif c_len > JSONLoader.colour_index:  # colours contain more than just 3 values (i.e. not RGB)
                raise ValueError("error in {}: colours exceed max number of values {}"
                                 .format(file_name, JSONLoader.colour_index))
            else:  # patterns/colours are verified - format patterns with corresponding RGB codes
                coloured_patterns = [[colours[j] for j in patterns[i]] for i in range(0, len(patterns))]
        except (FileNotFoundError, KeyError, IndexError, ValueError) as e:
            if sense is not None:
                sense.show_message(str(e), scroll_speed=0.04, back_colour=AbstractDisplay.err_colour)
            print(str(e))
            sys.exit()
        else:
            return coloured_patterns

    @staticmethod
    def get_range(arr: List[List[int]]):
        """
        utility method to find the min-item/max-item/max_length from a list of lists
        items are numeric values
        :param arr: a list of lists
        :returns: minimum value from any list, max value from any list, and max length of any list
        """
        a_min, a_max, a_len = 0, 0, 0
        for i in range(0, len(arr)):
            a_min = min(arr[i]) if a_min > min(arr[i]) else a_min
            a_max = max(arr[i]) if a_max < max(arr[i]) else a_max
            a_len = len(arr[i]) if a_len < len(arr[i]) else a_len
        return a_min, a_max, a_len
