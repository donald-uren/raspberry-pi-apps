"""
Main/driver class to run/halt program
"""

from threading import Thread
from monitorAndDisplay import TemperatureDisplay
from sense_hat import SenseHat, ACTION_PRESSED


def run_program():
    display = TemperatureDisplay("config.json")
    display_thread = Thread(target=display.run)
    display_thread.start()

    stop = False
    sense = SenseHat()
    while stop is False:
        events = sense.stick.get_events()
        for event in events:
            stop = True if event.action == ACTION_PRESSED else False

    display.terminate()


run_program()
