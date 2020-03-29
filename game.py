from electronicDie import ElectronicDice
from datetime import datetime
from sense_hat import SenseHat
from time import sleep
import csv

class Game:        
    def __init__(self, name1, name2):
        self.sense = SenseHat()
        self.dice = ElectronicDice()
        self.player1 = self.Player(name1)
        self.player2 = self.Player(name2)

    def run(self):
        self.display_message('instruction')
        while (self.player1.score < 30 and self.player2.score < 30):
            self.display_message("player 1 roll")
            score = self.dice.roll()
            self.player1.update_score(score)
            if self.player1.score >= 30:
                self.write_winner(self.player1)
                self.display_message('player 1 wins')
                break
            self.display_message("player 2 roll")
            score = self.dice.roll()
            self.player2.update_score(score)
            if self.player2.score >= 30:
                self.write_winner(self.player2)
                self.display_message('player 2 wins')
                break

    def display_message(self, message):
        if message == 'instruction':
            content = "Players take turn rolling the dice, who gets 30 points first win the game"
            print(content)
            self.sense.show_message(content, scroll_speed=0.05)
        elif message == 'player 1 wins':
            content = self.player1.name + ' wins'
            print(content)
            self.sense.show_message(content, scroll_speed=0.05)
        elif message == 'player 2 wins':
            content = self.player2.name + ' wins'
            print(content)
            self.sense.show_message(content, scroll_speed=0.05)
        elif message == 'player 1 roll':
            content = self.player1.name + "'s turn"
            print(content)
            self.sense.show_message(content, scroll_speed=0.05)
        elif message == 'player 2 roll':
            content = self.player2.name + "'s turn"
            print(content)
            self.sense.show_message(content, scroll_speed=0.05)

    def write_winner(self, player):
        with open('Desktop/winner.csv', mode='a') as winner_file:
            winner_writer = csv.writer(winner_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            winner_writer.writerow([datetime.now(), player.name, player.score])

    class Player:
        def __init__(self, name):
            self.name = name
            self.score = 0

        def update_score(self, score: int) -> int:
            self.score += score
            print(self.name + "'s score: " + str(self.score))
            return self.score

