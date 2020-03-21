from threading import Thread
from monitorAndDisplay import TemperatureDisplay
import time

stop = None
display = TemperatureDisplay()
display_thread = Thread(target=display.run())
while stop != "stop":
    stop = input("enter \'stop\' to halt program")
display.terminate()

