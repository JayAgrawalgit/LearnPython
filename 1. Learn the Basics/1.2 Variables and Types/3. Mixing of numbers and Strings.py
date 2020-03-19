# Mixing operators between numbers and strings is not supported:

one = 1
two = 2
three = "Hello"
print("one + two + three:",one + two + three)

# ERROR:
#   File "LearnPython/1. Learn the Basics/1.2 Variables and Types/3. Mixing of numbers and Strings.py", line 6, in <module>
#     print("one + two + three:",one + two + three)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Process finished with exit code 1
# EXPLAIN:
# Here it means that the operand '+' is not able to integer value and string value