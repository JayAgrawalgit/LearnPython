# To access a function inside of an object you use notation similar to accessing a variable:

class MyClass:
    variable = "First"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()

# The above would print out the message, "This is a message inside the class."

