"""
display and monitor temperature:
- update every 10s
- blue if <= cold_max
- red if >= hot_min
- else green
TODO: sep class/file for json handling?
TODO: separate display and reading from sense/writing to sense
"""
from sense_hat import SenseHat
from time import sleep
from threading import Thread
import json


class TemperatureDisplay:
    """
    TODO: display constantly, 10s is for reading temp > refactor function to display/functional separation
    TODO: ORRRR even easier is to just show a solid colour. no threads.
    TODO: ADD CLIBRATION CODE FROM LECTURE
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
        self.__temp = None
        self._running = True
        self.__sense = SenseHat()
        self.__cold, self.__hot = self.load_config(file_path)
        self.display_temperature()

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
        """
        TODO: sort out thread etc. maybe an easier way to do it. does it need to show constant? how to display constantly?
        :return:
        """
        update_thread = Thread(target=self.run_update)
        update_thread.start()
        while self._running:
            self.display_temperature()
            sleep(2)

    def run_update(self):
        while self._running:
            self.update_temperature()
            sleep(10)

    def terminate(self):
        self._running = False

    def update_temperature(self):
        self.__temp = self.__sense.get_temperature() + self.__adjustment

    def display_temperature(self):
        """
        Takes current temperature and displays in correct colour based on hot/cold range values
        NOTE: SenseHAT is consistently incorrect (overestimates temp), others have documented similar issues online
        Testing code in a SenseHAT emulator results in the correct output
        added self.__adjustment value to attempt to correct reading (wip)
        :return:
        """
        if self.__temp is not None:
            colour = self.blue if self.__temp <= self.__cold else (self.red if self.__temp >= self.__hot else self.green)
            temp_msg = '{: .0f}C'.format(self.__temp)
            self.__sense.show_message(temp_msg, text_colour=colour)
        else:
            self.__sense.show_message("Loading temp...")
