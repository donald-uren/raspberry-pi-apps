"""
display and monitor temperature:
- update every 10s
- blue if <= cold_max
- red if >= hot_min
- else green
TODO: use cron jobs? how does this run in background - tbc
TODO: sep class/file for json handling
"""
from sense_hat import SenseHat
from time import sleep
import json


class TemperatureDisplay:
    """
    Issue with senseHAT reading incorrect value (similar cases reported online)
    - rough adjustment to more closely align to correct temperature value
    """
    __adjustment = -5
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    def __init__(self, file_path):
        """
        Initialise object using file_path for range (hot/cold) values
        """
        self._running = True
        self.__sense = SenseHat()
        self.__cold, self.__hot = self.load_config(file_path)

    @staticmethod
    def load_config(file_path):
        """
        load range (hot/cold) values
        :param file_path: path of config.json file
        :return: hot/cold values
        """
        with open(file_path, "r") as fp:
            data = json.load(fp)
        return data["cold_max"], data["hot_min"]

    def run(self):
        while self._running:
            self.display_temperature()
            sleep(10)

    def terminate(self):
        self._running = False

    def display_temperature(self):
        """
        Takes current temperature and displays in correct colour based on hot/cold range values
        NOTE: SenseHAT is consistently incorrect (overestimates temp), others have documented similar issues online
        Testing code in a SenseHAT emulator results in the correct output
        TODO: put colours somewhere else? less hard-coded?
        :return:
        """
        temp = self.__sense.get_temperature() + self.__adjustment
        colour = self.blue if temp <= self.__cold else (self.red if temp >= self.__hot else self.green)
        temp_msg = '{: .0f}C'.format(self.__sense.get_temperature())
        self.__sense.show_message(temp_msg, text_colour=colour)
