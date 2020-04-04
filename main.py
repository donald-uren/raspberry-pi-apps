from animatedEmoji import EmojiDisplay
from threading import Thread
from sense_hat import SenseHat, ACTION_PRESSED


def run_program():
    """
    Creates thread to run application, and monitors for joystick press to stop program
    :return: None
    """
    display = EmojiDisplay("config.json")
    display_thread = Thread(target=display.display_emoji)
    display_thread.start()

    running = True
    sense = SenseHat()
    while running:
        events = sense.stick.get_events()
        for event in events:
            running = False if event.action == ACTION_PRESSED else True
    display.terminate()


run_program()
