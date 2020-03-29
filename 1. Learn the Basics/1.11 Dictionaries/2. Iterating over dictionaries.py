# Dictionaries can be iterated over, just like a list. However, a dictionary, unlike a list,
# does not keep the order of the values stored in it. To iterate over key value pairs, use the following syntax:

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

