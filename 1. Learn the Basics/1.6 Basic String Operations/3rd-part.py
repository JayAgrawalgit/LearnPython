astring = "Hello world!"
print(astring.upper())
print(astring.lower())
# These make a new string with all letters converted to uppercase and lowercase, respectively.


astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
# This is used to determine whether the string starts with something or ends with something, respectively.
# The first one will print True, as the string starts with "Hello".
# The second one will print False, as the string certainly does not end with "asdfasdfasdf".

astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)
# This splits the string into a bunch of strings grouped together in a list.
# Since this example splits at a space, the first item in the list will be "Hello", and the second will be "world!".