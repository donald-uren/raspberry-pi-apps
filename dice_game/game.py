from dice_game.electronicDie import ElectronicDice
from datetime import datetime
from sense_hat import SenseHat
import csv
import sys


class Game:
    """
    Game object
    """

    def __init__(self, names: list, file_path: str):
        self.sense = SenseHat()
        try:
            # Check if the players list is empty
            if len(names) <= 0:
                raise ValueError("Cannot run game with 0 players.")
        except ValueError as ve:
            self.sense.show_message(str(ve), scroll_speed=0.04)
            print(str(ve))
            sys.exit()
        else:
            self.dice = ElectronicDice()
            # using the names list parameter, creates a dictionary of Player objects
            self.players = {i + 1: self.Player(names[i]) for i in range(0, len(names))}
            self.max_players = len(names)
            self.max_score = 30
            self.file_path = file_path

    def run(self):
        """
        Runs the game: iterates over player list, stopping if a player reaches self.max_score
        :return: void
        """
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
            # set the current player to the first if the round has ended
            if curr_player == self.max_players:
                scores = ", ".join([str(player) for player in self.players.values()])
                scores_format = "Round {} scores: {}".format(round_count, scores)
                self.display_message(msg=scores_format)
                round_count += 1
                curr_player = 1
            else:
                curr_player += 1

    def display_message(self, msg, init=False, win=False, index=None):
        """
        displays a message on the SenseHat
        :param msg: information to show - required parameter
        :param init: flag to indicate introductory instructions/rules at start of game
        :param win: flag to indicate a player has one
        :param index: index of a player in dictionary self.players
        :return: void
        """
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

    def write_winner(self, player):
        """
        Write winner and their score to the csv file with a timestamp
        :param player: player object (winner of the game)
        :return: void
        """
        try:
            with open(self.file_path, mode='a') as winner_file:
                winner_writer = csv.writer(winner_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                winner_writer.writerow([datetime.now(), player.name, player.score])
        except IOError as io:
            print('Failed to open file.\n{}'.format(str(io)))
            self.sense.show_message(str(io), scroll_speed=0.04)

    class Player:
        """
        Player object has a name and a score
        """

        def __init__(self, name):
            self.name = name
            self.score = 0

        def update_score(self, score: int) -> int:
            """
            update_score method add dice result to player score
            :param score: amount update by
            :return: player score
            """
            self.score += score
            return self.score

        def __str__(self):
            return "{}'s score: {}".format(self.name, self.score)
