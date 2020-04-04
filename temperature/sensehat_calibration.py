# Reference: https://raspberrypi.stackexchange.com/questions/61524/how-to-approximate-room-temperature-in-a-better-way
"""
Code sourced from: PIOT_LECTURE4_CODEARCHIVE - 05_sensehat_calibration
    permitted to be used in assignment - see lecture 4 recording
"""
import os
from sense_hat import SenseHat


class CalibratedSenseHat(SenseHat):
    """
    Extends SenseHat and overrides get_temperature to enable calibration/correction for CPU temperature.
    """

    def __init__(self):
        super().__init__()

    def get_temperature(self):
        """
        Overrides SenseHat.get_temperature(), adding in calibration/correction for CPU temperature
        :return: void
        """
        temp_cpu = get_cpu_temp()
        # Calculates the real temperature compensating CPU heating.
        temp_avg = (self.get_temperature_from_humidity() + self.get_temperature_from_humidity()) / 2
        calibrated = temp_avg - ((temp_cpu - temp_avg) / 1.2)
        calibrated = get_smooth(calibrated)
        return calibrated

    def show_message(self, text_string, scroll_speed=.04, text_colour=None, back_colour=None):
        if back_colour is None:
            back_colour = [0, 0, 0]
        if text_colour is None:
            text_colour = [255, 255, 255]
        super().show_message(text_string, scroll_speed, text_colour, back_colour)


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
