# Lists are very similar to arrays.
# They can contain any type of variable, and they can contain as many variables as you wish.
# Lists can also be iterated over in a very simple manner.
# It will store memory dynamically.
# Here is an example of how to build a list.
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
for x in mylist:
    print(x)       # here it will print value available at it's index 1,2,3.
print(mylist)       # here it will print mylist available as it is.


# Accessing an index which does not exist generates an exception (an error).
print(mylist[10])           # IndexError: list index out of rang