# Reference: https://raspberrypi.stackexchange.com/questions/61524/how-to-approximate-room-temperature-in-a-better-way
import os
from sense_hat import SenseHat


class CalibratedSenseHat(SenseHat):
    def __init__(self):
        super().__init__()

    def get_temperature(self):
        t_cpu = get_cpu_temp()
        # Calculates the real temperature compensating CPU heating.
        t = (self.get_temperature_from_humidity() + self.get_temperature_from_humidity()) / 2
        t_corr = t - ((t_cpu - t) / 1.5)
        t_corr = get_smooth(t_corr)
        return t_corr


# Get CPU temperature.
def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=", "").replace("'C\n", ""))


# Use moving average to smooth readings.
def get_smooth(x):
    if not hasattr(get_smooth, "t"):
        get_smooth.t = [x, x, x]
    get_smooth.t[2] = get_smooth.t[1]
    get_smooth.t[1] = get_smooth.t[0]
    get_smooth.t[0] = x
    return (get_smooth.t[0] + get_smooth.t[1] + get_smooth.t[2]) / 3