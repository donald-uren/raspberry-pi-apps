from animatedEmoji import EmojiDisplay
from threading import Thread
from sense_hat import SenseHat, ACTION_PRESSED
from application import Application
import sys


def process_input():
    sense = SenseHat()
    if len(sys.argv) <= 1:
        sense.show_message("Incorrect args: {}\nexpected main.py [emoji|temperature] filepath".format(" ".join(sys.argv)))
    else:
        app = sys.argv[1]
        config = sys.argv[2] if len(sys.argv) > 2 else None
        print(app == "emoji")
        if app == "emoji":
            display = EmojiDisplay(config)
        elif app == "temperature":
            sense.show_message("temp")
            display = EmojiDisplay(config)
        else:
            display = EmojiDisplay(config)
        run_program(display, sense)


def run_program(application: Application, sense: SenseHat):
    """
    Creates thread to run application, and monitors for joystick press to stop program
    :return: None
    """
    display_thread = Thread(target=application.run)
    display_thread.start()

    running = True
    while running:
        events = sense.stick.get_events()
        for event in events:
            running = False if event.action == ACTION_PRESSED else True
    application.terminate()


process_input()
