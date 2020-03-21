from threading import Thread
from monitorAndDisplay import TemperatureDisplay
import time

stop = None
display = TemperatureDisplay()
display_thread = Thread(target=display._run())
while stop != "stop":
    stop = input("enter \'stop\' to halt program")
display._terminate()

