# Packages are namespaces which contain multiple packages and modules themselves. They are simply directories, but with a twist.
# Each package in Python is a directory which MUST contain a special file called __init__.py. This file can be empty,
# and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can
# be imported. If we create a directory called foo, which marks the package name, we can then create a module inside
# that package called bar. We also must not forget to add the __init__.py file inside the foo directory.
# To use the module bar, we can import it in two ways:

import foo.bar
# or:
from foo import bar


# In the first method, we must use the foo prefix whenever we access the module bar. In the second method, we don't,
# because we import the module to our module's namespace.
# The __init__.py file can also decide which modules the package exports as the API, while keeping other modules
# internal, by overriding the __all__ variable, like so:


__init__.py:
__all__ = ["bar"]
