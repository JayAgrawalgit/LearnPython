# To access the variable inside of the newly created object "myobjectx" you would do the following:

class MyClass:
    variable = "First"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjectx.variable
# So for instance the below would output the string "blah":


# You can create multiple different objects that are of the same class(have the same variables and functions defined).
# However, each object contains independent copies of the variables defined in the class.
myobjecty = MyClass()
print(myobjecty.variable)


# For instance,
# if we were to define another object with the "MyClass" class and then change the string in the variable above:
myobjecty.variable = "Second"


# Then print out both values
print(myobjectx.variable)           # First
print(myobjecty.variable)           # Second