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

# The draw module may look something like this:
# draw.py
def draw_game():
    ...

def clear_screen(screen):
    ...

# In this example, the game module imports the draw module, which enables it to use functions implemented in that module.
# The main function would use the local function play_game to run the game, and then draw the result of the game using
# a function implemented in the draw module called draw_game. To use the function draw_game from the draw module,
# we would need to specify in which module the function is implemented, using the dot operator. To reference the
# draw_game function from the game module, we would need to import the draw module and only then call draw.draw_game().
# When the import draw directive will run, the Python interpreter will look for a file in the directory which the
# script was executed from, by the name of the module with a .py prefix, so in our case it will try to look for draw.py.
# If it will find one, it will import it. If not, he will continue to look for built-in modules.
# You may have noticed that when importing a module, a .pyc file appears, which is a compiled Python file.
# Python compiles files into Python bytecode so that it won't have to parse the files each time modules are loaded.
# If a .pyc file exists, it gets loaded instead of the .py file, but this process is transparent to the user.