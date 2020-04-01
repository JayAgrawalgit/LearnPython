# In programming, a module is a piece of software that has a specific functionality.
# For example, when building a ping pong game, one module would be responsible for the game logic, and
# another module would be responsible for drawing the game on the screen. Each module is a different file,
# which can be edited separately.

# Modules in Python are simply Python files with a .py extension. The name of the module will be the name of the file.
# A Python module can have a set of functions, classes or variables defined and implemented. In the example above,
# we will have two files, we will have:

mygame/
mygame/game.py
mygame/draw.py

# The Python script game.py will implement the game. It will use the function draw_game from the file draw.py,
# or in other words, thedraw module, that implements the logic for drawing the game on the screen.

# Modules are imported from other modules using the import command. In this example,
# the game.py script may look something like this:


# game.py
# import the draw module
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()