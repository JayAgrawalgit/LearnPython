# To access the variable inside of the newly created object "myobjectx" you would do the following:

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjectx.variable


# So for instance the below would output the string "blah":
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
print(myobjectx.variable)

#
# You can create multiple different objects that are of the same class(have the same variables and functions defined).
# However, each object contains independent copies of the variables defined in the class.
# For instance,
# if we were to define another object with the "MyClass" class and then change the string in the variable above:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)