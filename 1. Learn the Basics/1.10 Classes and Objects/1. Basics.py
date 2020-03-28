# Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes. Classes are essentially a template to create your objects.
# A very basic class would look something like this:

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

# We'll explain why you have to include that "self" as a parameter a little bit later.
# First, to assign the above class(template) to an object you would do the following:

class MyClass1:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass1()


# Now the variable "myobjectx" holds an object of the class "MyClass" that contains the variable and
# the function defined within the class called "MyClass".



