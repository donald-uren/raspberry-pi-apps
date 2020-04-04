from temperature.virtual_sense_hat import VirtualSenseHat
from display import AbstractDisplay
from time import sleep
import sys
import json


class TemperatureDisplay(AbstractDisplay):
    """
    Displays and monitors current temperature:
    - updates every 10s
    - display blue if <= cold_max
    - display red if >= hot_min
    - else display green
    overrides run() from abstract class Application - refer to display.py for details
    """
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    def __init__(self, file_path):
        """
        Initialise object, loads range values from configuration, and SenseHat (if available)
        :param file_path: config.json file path
        """
        super().__init__()
        self._sense = VirtualSenseHat.getSenseHat()
        self._hot, self._cold = JSONLoader.load_config(file_path, self._sense)

    def run(self):
        """
        Records current temperature and runs temperature display (until joystick pressed)
        :return: void
        """
        while self._running:
            temp = self._sense.get_temperature()
            self.display_temperature(temp)
            sleep(10)
        self._sense.clear()

    def display_temperature(self, temp):
        """
        Takes current temperature and displays in correct colour based on hot/cold range values.

        NOTE: the SenseHat I've been working with doesn't detect the correct temperature. I've applied (and modified)
        the calibration code from PIOT_LECTURE4_CODEARCHIVE however it's still off by roughly 2C.

        :param temp: current temperature reading from CalibratedSenseHat [see CalibratedSenseHat.get_temperature()]
        :return: void
        """
        colour = self.blue if temp <= self._cold else (self.red if temp >= self._hot else self.green)
        self._sense.clear(colour)
        # print temperature value to console for verification
        print("{: .1f}C".format(temp))


class JSONLoader:
    """
    Expected configuration of config.json file is:
        cold_max: x,
        hot_min: y
    where x < y
    - only two range values are required i.e. comfortable range can be assumed from maximum of cold and minimum of hot
    """

    @staticmethod
    def load_config(file_path, sense):
        """
        attempts to load config.json file from
        :param file_path: path of config.json file
        :param sense: CalibratedSenseHat object for displaying error messages
        :return: hot/cold values (if correct)
        """
        try:
            with open(file_path, "r") as fp:
                data = json.load(fp)
            cold = data["cold_max"]
            hot = data["hot_min"]
            if hot < cold:
                raise ValueError("Error in range values: hot = {} cold = {}".format(hot, cold))
        except (FileNotFoundError, KeyError, ValueError) as e:
            message = str(e)
            sense.show_message(message, back_colour=AbstractDisplay.err_colour)
            print(message)
            sys.exit()
        else:
            return hot, cold
