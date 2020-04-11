# The target of this exercise is to create a string, an integer, and a floating point number.
# The string should be named mystring and should contain the word "hello".
# The floating point number should be named myfloat and should contain the number 10.0,
# and the integer should be named myint and should contain the number 20.
# Inisiation
mystring = "hello"
myfloat = 10.0
myint = 20


# testing code
if isinstance( mystring , str):
    print("Mystring(",mystring,") is a string")
if isinstance( myfloat , float):
    print("myfloat(%f) is a float value" % myfloat)
if isinstance( myint , int):
    print("myfloat(%d) is a float value" % myint)


# here isinstance is a predefine python function for checking the variables types
# it can check float, int, str, list, dict, tuple and instance.
# this all topics we will discourse farther in module
# And if you want to print any value in medial of the sentence
# then you can write print as per used in if 
# for more Variables you can use
# int = %d
# float = %f
# str = %s
# character = %c
