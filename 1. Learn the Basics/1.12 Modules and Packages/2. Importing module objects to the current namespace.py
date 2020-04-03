# We may also import the function draw_game directly into the main script's namespace, by using the from command.

# game.py
# import the draw module
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)

# You may have noticed that in this example, draw_game does not precede with the name of the module it is imported from,
# because we've specified the module name in the import command.
# The advantages of using this notation is that it is easier to use the functions inside the current module because you
# don't need to specify which module the function comes from. However, any namespace cannot have two objects with the
# exact same name, so the import command may replace an existing object in the namespace.

