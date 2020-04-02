# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.
# Each value stored in a dictionary can be accessed using a key,
# which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.
# For example, a database of phone numbers could be stored using a dictionary like this:

phonebook = {}
phonebook["John"] = 938477561
phonebook["Jack"] = 938377262
phonebook["Jill"] = 947662783
print(phonebook)


# Alternatively, a dictionary can be initialized with the same values in the following notation:

phonebook2 = {
    "Jony" : 938477564,
    "Jay" : 938377265,
    "Jeny" : 947662786
}
print(phonebook2)