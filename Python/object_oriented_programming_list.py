# Object Orientation: Object-Oriented Programming (OOP)
# OOP is an approach to organize or structure your code. It breaks a program into smaller parts known as objects using the Class blueprint
# Objects can communicate with each other to make a program function but the division into smaller units makes the code easier to reuse and maintain
# Each of these objects has its unique attributes/properties and behaviours/methods. 
# Attributes are the data that the object has and Behaviours are something that the object can do
# You create objects using a blueprint known as class
# A class describes the types of attributes and behaviours that an object should have. You can use the same class to build multiple objects based on the same pattern but containing different property values.
# eg. a class that created list objects 
# Each time you create a list, your list is created based on Python's built-in class Array, which inherits all behaviours or methods from the array. Similarly, when you create a Python list you inherit all methods from the list class.  This ensures that objects only have methods that they need to avoid needlessly overloading computer memory with unnecessary extra methods, at the same time, this OOP to organization method allows for easily creating new data objects and immediately using the most common methods to work with that data, OOP frees us up from repetitively building the same basic building blocks, more time to build the functionality and features we want in the program 
 

# A list that logs the sequence of results of five coin flips

flips = [
    'heads',
    'tails',
    'tails',
    'heads',
    'tails',
]

print(flips.count('heads')) # Use the count method to return the number of elements that match a certain string 'heads'
print(flips.pop()) # Using the pop() method will return the final element in the list
