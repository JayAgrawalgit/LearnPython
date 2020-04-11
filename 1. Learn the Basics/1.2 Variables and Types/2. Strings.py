# Strings are defined either with a single quote or a double quotes.
mystring = 'hello'
print("In single quote:",mystring)
mystring = "hello"
print("In double quotes:",mystring)


# The difference between the two is that using double quotes makes it easy to include apostrophe.
# (whereas these would terminate the string if using single quotes)
mystring = "Don't thing about apostrophe"
print("Because double quotes:",mystring)


# There are additional variations on defining strings that make it easier to include things such as carriage returns,
# backslashes and Unicode characters. These are beyond the scope of this tutorial, but are covered in the Python
# documentation.
# Simple operators can be executed on numbers and strings:
one = 1
two = 2
three = one + two
print("Three prints:",three)
hello = "Hello"
world = "World!"
helloworld = hello + " " + world
print("helloworld key word print's:",helloworld)
