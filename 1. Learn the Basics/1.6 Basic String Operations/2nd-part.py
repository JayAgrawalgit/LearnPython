astring = "Hello world!"
print(astring[3:7])
# This prints a slice of the string, starting at index 3, and ending at index 6.
# But why 6 and not 7? Again, most programming languages do this - it makes doing math inside those brackets easier.


# If you just have one number in the brackets, it will give you the single character at that index.
#If you leave out the first number but keep the colon, it will give you a slice from the start to the number you left in
# If you leave out the second number, it will give you a slice from the first number to the end.

# You can even put negative numbers inside the brackets.
# They are an easy way of starting at the end of the string instead of the beginning.
# This way, -3 means "3rd character from the end".
astring = "Hello world!"
print(astring[3:7:2])
# This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax.
# The general form is [start:stop:step].


astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])
# Note that both of them produce same output

# There is no function like strrev in C to reverse a string.
# But with the above mentioned type of slice syntax you can easily reverse a string like this
astring = "Hello world!"
print(astring[::-1])        # !dlrow olleH