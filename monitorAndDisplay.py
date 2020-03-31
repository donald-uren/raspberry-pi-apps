"""
display and monitor temperature:
- update every 10s
- blue if <= cold_max
- red if >= hot_min
- else green
"""
from virtual_sense_hat import VirtualSenseHat
from time import sleep
import sys
import json


class TemperatureDisplay:
    """
    Issue with senseHAT reading incorrect value (similar cases reported online)
    - rough adjustment to more closely align to correct temperature value
    """
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    def __init__(self, file_path):
        """
        Initialise object using file_path for range (hot/cold) values
        """
        self._running = True
        self._sense = VirtualSenseHat.getSenseHat()
        # self._sense = VirtualSenseHat.getVirtualSenseHat()
        self._hot, self._cold = JSONLoader.load_config(file_path, self._sense)

    # @staticmethod
    # def load_config(file_path):
    #     """
    #     load range (hot/cold) values
    #     :param file_path: path of config.json file
    #     :return: hot/cold values
    #     """
    #     with open(file_path, "r") as fp:
    #         data = json.load(fp)
    #     return data["cold_max"], data["hot_min"]

    def run(self):
        """
        :return:
        """
        while self._running:
            temp = self._sense.get_temperature()
            self.display_temperature(temp)
            sleep(10)

    def terminate(self):
        self._sense.clear()
        self._running = False

    def display_temperature(self, temp):
        """
        Takes current temperature and displays in correct colour based on hot/cold range values
        NOTE: SenseHAT is consistently incorrect (overestimates temp), others have documented similar issues online
        Testing code in a SenseHAT emulator results in the correct output
        added self.__adjustment value to attempt to correct reading (wip)
        :param temp: current temperature reading from CalibratedSenseHat [see get_temperature()]
        :return: None
        """
        colour = self.blue if temp <= self._cold else (self.red if temp >= self._hot else self.green)
        # if temp <= self._cold:
        #     colour = self.blue
        # elif temp >= self._hot:
        #     colour = self.red
        # else:
        #     colour = self.green
        self._sense.clear(colour)
        # print temperature value to console for verification
        print("{: .1f}C".format(temp))


class JSONLoader:
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
                raise ValueError("Hot cannot be less than cold value")
        except FileNotFoundError as fnfe:
            message = "Could not find {}\n".format(file_path)
            sense.show_message(message)
            print("{}\n{}".format(message, str(fnfe)))
            sys.exit()
        except KeyError as ke:
            message = "Error in accessing range values in {}\n".format(file_path)
            sense.show_message(message)
            print("{}\n{}".format(message, str(ke)))
            sys.exit()
        except ValueError as ve:
            message = "Error in range values:\n{}".format(ve)
            sense.show_message(message)
            print("{}\n{}".format(message, str(ve)))
            sys.exit()
        else:
            return hot, cold
