# In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method.
# You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.
# You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator [].
# Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.
# Ans:

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]
for x in range (1,4):
    numbers.append(x)
x = "Hello World!"
strings = x.split()
second_name = None

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# here we use 2 funcrtion
# 1. append:
#       it is use for add value into list
#       syntax: list_name.append(value)

# 2. split:
#       it is mostly use for strings sepretion