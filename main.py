from threading import Thread
from monitorAndDisplay import TemperatureDisplay
import time

display = TemperatureDisplay()
display._run()
print('type \'stop\' to halt program.')

