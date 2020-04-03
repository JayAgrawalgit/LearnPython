# There are a couple of ways we could tell the Python interpreter where to look for modules, aside from the default,
# which is the local directory and the built-in modules. You could either use the environment variable PYTHONPATH to
# specify additional directories to look for modules in, like this:

PYTHONPATH=/foo python game.py

# This will execute game.py, and will enable the script to load modules from the foo directory as well as the local directory.

# Another method is the sys.path.append function. You may execute it before running an import command:

sys.path.append("/foo")

# This will add the foo directory to the list of paths to look for modules in as well.
