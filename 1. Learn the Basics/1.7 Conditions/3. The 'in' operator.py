# The "in" operator could be used to check if a specified object exists within an iterable object container,
# such as a list:
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

# Python uses indentation to define code blocks, instead of brackets.
# The standard Python indentation is 4 spaces, although tabs and any other space size will work,
# as long as it is consistent. Notice that code blocks do not need any termination.

# Here is an example for using Python's "if" statement using code blocks:
statement = False
another_statement = True
if statement is True:
    print(True)
    pass
elif another_statement is True: # else if
    print(True)
    pass
else:
    print(False)
    pass

# A statement is evaulated as true if one of the following is correct:
# 1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison.
# 2. An object which is not considered "empty" is passed.

