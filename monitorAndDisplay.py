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


class TemperatureDisplay:
    # create static range variables?
    def __init__(self):
        """
        TODO: add cold/hot values upon init?
        - static for class? all objects need the same, maybe outside of init?
        """
        self.__sense = SenseHat()
        self.__cold = 10
        self.__hot = 25

    def display_temperature(self):
        """
        TODO: this method runs every 10s, grab current temp and display
        :return:
        """
        colour = None
        temp = self.__sense.get_temperature()
        if temp <= self.__cold:
            colour = (0, 0, 255)
        elif temp >= self.__hot:
            colour = (255, 0, 0)
        else:
            colour = (0, 255, 0)
        temp_msg = '{: .0f}C'.format(self.__sense.get_temperature())
        self.__sense.show_message(temp_msg, text_colour=colour)
