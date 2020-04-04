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
        round_count = 1
        curr_player = 1
        self.display_message(msg=self.max_score, init=True)
        while True:
            player = self.players.get(curr_player)
            self.display_message(msg=player.name, index=curr_player)
            player.update_score(self.dice.roll())
            if player.score >= self.max_score:
                self.write_winner(player)
                self.display_message(msg=player.name, win=True, index=curr_player)
                break
            if curr_player == self.max_players:
                scores = ", ".join([str(player) for player in self.players.values()])
                scores_format = "Round {} scores: {}".format(round_count, scores)
                self.display_message(msg=scores_format)
                round_count += 1
                curr_player = 1
            else:
                curr_player += 1

    def display_message(self, msg, init=False, win=False, index=None):
        if init:
            message = "Players take turns rolling the dice, the first to get {} points wins the game".format(msg)
        elif win:
            message = "{} (player {}) wins!".format(msg, index)
        elif index is not None:
            message = "{}'s roll (player {})".format(msg, index)
        else:
            message = msg
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
