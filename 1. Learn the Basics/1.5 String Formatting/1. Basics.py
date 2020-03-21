# Python uses C-style string formatting to create new, formatted strings.
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list),
# together with a format string, which contains normal text together with "argument specifiers",
# special symbols like "%s" and "%d". Let's say you have a variable called "name" with your user name in it,
# and you would then like to print(out a greeting to that user.)
# This prints out "Hello, John!"
name = "Jay"
print("Hello, %s" % name)       #Hello, Jay
# or we can use directly
print("Hello,",name)            #Hello, Jay


# To use two or more argument specifiers, use a tuple (parentheses):
name = "John"
age = 23
print("%s is %d years old." % (name, age))
# output will be "John is 23 years old."


# Any object which is not a string can be formatted using the %s operator as well.
# The string which returns from the "repr" method of that object is formatted as the string. For example:
# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)
