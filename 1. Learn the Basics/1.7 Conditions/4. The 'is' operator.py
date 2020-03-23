# Unlike the double equals operator "==", the "is" operator does not match the values of the variables,
# but the instances themselves. For example:
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False
# The is operator compares the identity of two objects while the == operator compares the values of two objects.\
# The is operator evaluates to true if the variables on either side of the operator point to the same object and false otherwise.