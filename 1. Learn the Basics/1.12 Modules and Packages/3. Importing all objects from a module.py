# We may also use the import * command to import all objects from a specific module, like this:

# game.py
# import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)


# This might be a bit risky as changes in the module might affect the module which imports it, but it is shorter and
# also does not require you to specify which objects you wish to import from the module.

