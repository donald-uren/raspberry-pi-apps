from emoji.animatedEmoji import EmojiDisplay
from temperature.monitorAndDisplay import TemperatureDisplay
from threading import Thread
from sense_hat import SenseHat, ACTION_PRESSED
from display import AbstractDisplay
import sys


def process_input():
    """
    interprets the command line input, running either TemperatureDisplay or EmojiDisplay
    For Temperature display, verifies that config file is .json format as per requirements
    (the config file is an optional argument for EmojiDisplay)
    :return:
    """
    sense = SenseHat()
    try:
        if len(sys.argv) > 1:
            app = sys.argv[1]
            # argv[2] specifies the config.json file (if required)
            config = sys.argv[2] if len(sys.argv) > 2 else None
            if app == "emoji":
                display = EmojiDisplay(config)
            elif app == "temperature":
                if config is not None and config.endswith(".json"):
                    display = TemperatureDisplay(config)
                else:
                    raise ValueError("Incorrect config file: {}".format(config))
            else:
                raise ValueError("Incorrect application name: {}".format(app))
        else:
            raise ValueError(
                "Incorrect args: {}\nexpected main.py [emoji|temperature] [filepath]".format(" ".join(sys.argv)))
    except ValueError as ve:
        print(str(ve))
        sense.show_message(str(ve), scroll_speed=0.04, text_colour=[255, 0, 0])
    else:
        run_program(display, sense)


def run_program(application: AbstractDisplay, sense: SenseHat):
    """
    Creates thread to run application, and monitors for joystick press to stop program
    Uses Application as an interface, where EmojiDisplay/TemperatureDisplay implement the abstract methods
    :return: void
    """
    display_thread = Thread(target=application.run)
    display_thread.start()

    running = True
    while running:
        # get a list of joystick events from sense_hat
        events = sense.stick.get_events()
        for event in events:
            # halts program if any direction or click is pressed by user
            running = False if event.action == ACTION_PRESSED else True
    application.terminate()


process_input()
