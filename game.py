from electronicDie import ElectronicDice
from datetime import datetime
from sense_hat import SenseHat
import csv
import sys


# Game object
class Game:
    def __init__(self, names: list, file_path: str):
        try:
            # Check if the players list is empty
            if len(names) <= 0:
                raise ValueError("Cannot run game with 0 players.")
        except ValueError as ve:
            print(str(ve))
            sys.exit()
        else:
            self.sense = SenseHat()
            self.dice = ElectronicDice()
            self.players = {i + 1: self.Player(names[i]) for i in range(0, len(names))}
            self.max_players = len(names)
            self.max_score = 30
            self.file_path = file_path

    # Run the game
    def run(self):
        curr_player = 1
        # Display init game instruction
        self.display_message(init=True)
        while True:
            # Loop through players list and record their score
            player = self.players.get(curr_player)
            self.display_message(index=curr_player, name=player.name)
            player.update_score(self.dice.roll())
            # If player score is greater than max score then start end game protocol
            if player.score >= self.max_score:
                self.write_winner(player)
                self.display_message(win=True, index=curr_player, name=player.name)
                break
            # iterate to next player in player list
            curr_player = 1 if curr_player == self.max_players else curr_player + 1

    # Display appropriate messages through out a game
    def display_message(self, win=False, index=None, name=None, init=False):
        if init:
            message = "Players take turns rolling the dice, the first to get {} points wins the game".format(
                self.max_score)
        elif win:
            message = "{} (player {}) wins!".format(name, index)
        else:
            message = "{}'s roll (player {})".format(name, index)
        print(message)
        self.sense.show_message(message, scroll_speed=0.04)

    # Write winner and their score to the csv file with a timestamp
    def write_winner(self, player):
        try:
            with open(self.file_path, mode='a') as winner_file:
                winner_writer = csv.writer(winner_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                winner_writer.writerow([datetime.now(), player.name, player.score])
        except IOError as io:
            print('Failed to open file.\n{}'.format(str(io)))

    # Player object has a name and a score
    class Player:
        def __init__(self, name):
            self.name = name
            self.score = 0

        # update_score method add dice result to player score
        def update_score(self, score: int) -> int:
            self.score += score
            return self.score

        def __str__(self):
            return "{}'s score: {}".format(self.name, self.score)
