# To remove a specified index, use either one of the following notations:

phonebook = {
   "John" : 938477561,
   "Jack" : 938377262,
   "Jill" : 947662783
}
del phonebook["John"]
print(phonebook)

# or:

phonebook2 = {
    "Jony" : 938477564,
    "Jay" : 938377265,
    "Jeny" : 947662786
}
phonebook2.pop("Jony")
print(phonebook2)