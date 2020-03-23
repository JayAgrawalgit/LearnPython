# Strings are bits of text. They can be defined as anything between quotes:
astring = "Hello world!"
astring2 = 'Hello world!'
print(astring,astring2)


# As you can see, the first thing you learned was printing a simple sentence.
# This sentence was stored by Python as a string. However, instead of immediately printing strings out,
# we will explore the various things you can do to them. You can also use single quotes to assign a string.
# However, you will face problems if the value to be assigned itself contains single quotes.
# For example to assign the string in these bracket(single quotes are ' ') you need to use double quotes only like this
astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))
# That prints out 12, because "Hello world!" is 12 characters long, including punctuation and spaces.


astring = "Hello world!"
print(astring.index("o"))
# That prints out 4, because the location of the first occurrence of
# the letter "o" is 4 characters away from the first character.
# Notice how there are actually two o's in the phrase - this method only recognizes the first.
#
#
# But why didn't it print out 5? Isn't "o" the fifth character in the string? To make things more simple,
# Python (and most other programming languages) start things at 0 instead of 1. So the index of "o" is 4.
astring = "Hello world!"
print(astring.count("l"))
# For those of you using silly fonts, that is a lowercase L, not a number one.
# This counts the number of l's in the string. Therefore, it should print 3.