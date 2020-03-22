"""
Main/driver class to run/halt program
"""

from threading import Thread
from monitorAndDisplay import TemperatureDisplay

display = TemperatureDisplay("config.json")
display_thread = Thread(target=display.run)
display_thread.start()

stop = None
while stop != "stop":
    stop = input("enter \'stop\' to halt program.\n")

display.terminate()
