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