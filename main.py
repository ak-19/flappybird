from setup import Setup

from game import Game

setup = Setup()

game = Game(setup.get_display())

game.run_game_loop()

setup.quit()