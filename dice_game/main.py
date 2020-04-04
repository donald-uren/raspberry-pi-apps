from dice_game.game import Game

# Start a game with 2 parameters:
# A list of players and.
# A csv file name to export the result to
game = Game(["John", "Mike"], "winner.csv")
game.run()
