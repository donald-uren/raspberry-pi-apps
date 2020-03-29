from electronicDie import ElectronicDie
from datetime import datetime
from sense_emu import SenseHat
import csv

class Game:        
    def __init__(self, name1, name2):
        self.sense = SenseHat()
        self.die = ElectronicDie()
        self.player1 = self.Player(name1)
        self.player2 = self.Player(name2)

    def run(self):
        self.display_message('instruction')
        while (self.player1.score < 30 and self.player2.score < 30):
            self.display_message("Player 1's turn")
            score = self.die.roll()
            self.player1.update_score(score)
            if self.player1.score >= 30:
                self.write_winner(self.player1)
                self.display_message('player 1 win')
                break
            self.display_message("Player 2's turn")
            score = self.die.roll()
            self.player2.update_score(score)
            if self.player2.score >= 30:
                self.write_winner(self.player2)
                self.display_message('player 2 win')
                break

    def display_message(self, message):
        if message == 'instruction':
            self.sense.show_message('game')
        elif message == 'player 1 win':
            self.sense.show_message('Player 1 win')
        elif message == 'player 2 win':
            self.sense.show_message('Player 2 win')
        elif message == 'player 1 roll':
            self.sense.show_message("Player 1's turn")
        elif message == 'player 2 roll':
            self.sense.show_message("Player 2's turn")

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
            return score

game = Game('John', 'Mike')
game.run()
