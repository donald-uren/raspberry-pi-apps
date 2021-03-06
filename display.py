from abc import ABC, abstractmethod


class AbstractDisplay(ABC):
    """
    Simple abstract class for use in Task A & B
    """
    err_colour = [255, 0, 0]

    def __init__(self):
        """
        Sets up initial loop condition. While True, the application will continue to run
        """
        self._running = True
        # used to display errors on sense_hat in red

    @abstractmethod
    def run(self):
        """
        implemented in EmojiDisplay and TemperatureDisplay
        used to begin the looping of the program
        follows basic structure of:
            while self._running:
                ...
                iterate/run program
                ...
            sense.clear()
        :return: void
        """
        ...

    def terminate(self):
        """
        sets the loop condition to false, i.e. will halt program after current iteration completes
        :return: void
        """
        self._running = False
