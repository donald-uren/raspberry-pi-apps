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


def load_config():
    with open("config.json", "r") as fp:
        data = json.load(fp)
    return data["cold_max"], data["hot_min"]


class TemperatureDisplay:
    # create static range variables?
    def __init__(self):
        """
        TODO: add cold/hot values upon init?
        - static for class? all objects need the same, maybe outside of init?
        """
        self._running = True
        self.__sense = SenseHat()
        self.__cold, self.__hot = load_config()

    def run(self):
        while self._running:
            self.display_temperature()
            sleep(10)

    def terminate(self):
        self._running = False

    def display_temperature(self):
        """
        NOTE: SenseHAT is consistently incorrect (overestimates temp), others have documented similar issues online
        Testing code in a SenseHAT emulator results in the correct output
        TODO: this method runs every 10s, grab current temp and display
        TODO: put colours somewhere else? less hard-coded?
        :return:
        """

        temp = self.__sense.get_temperature()
        if temp <= self.__cold:
            colour = (0, 0, 255)
        elif temp >= self.__hot:
            colour = (255, 0, 0)
        else:
            colour = (0, 255, 0)
        temp_msg = '{: .0f}C'.format(self.__sense.get_temperature())
        self.__sense.show_message(temp_msg, text_colour=colour)
