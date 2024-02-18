# Program to print attendee names and tickets ordered using class
# Creating a class with the keyword class
# The first, def --init-- constructor function to specify what happens when you use the class in your code. When you use the class, you specify the name and the ticket parameters, which are saved in the new object

# The remaining two def statements in the class, define methods that become part of any object that you create based on that class. The first one prints the name and ticket value for the current object(displayAttendee). The second one, add ticket, allows to increase the number of tickets by one that are assigned to an attendee 


class Attendee: # creating a class with a name 
    'Common base class for all attendees' # description of class

    def __init__(self, name, tickets):  # constructor function with parameters
        self.name = name
        self.tickets = tickets

    def displayAttendee(self): # printa name and ticket value for the current object
        print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

    def addTicket(self):
        self.tickets += 1
        print('{} tickets increased to {}'.format(self.name, self.tickets))

# Now, we will use our class in some code
# create a variable attendee1, use Attendee class, pass two parameters to it, name B. giles and ticket 2. The result of this statement will be an object that stores these two properties using the names name and tickets. This new object will also include the displayAttendee and addTicket method that are part of the class it was created from.
                
attendee1 = Attendee('B. giles', 2)

# Create another custom object the same way. attendee2 object has different name and ticket properties values but it shares the same displayAttendee and addTicket methods
attendee2 = Attendee('J. Ortega', 1) 

# Use the methods from the class to work with these objects that we created

attendee1.displayAttendee() # prints the name and tickets values with labels, this makes it easier to understand the values that are stored in these objects
attendee2.displayAttendee()


# Imagine attendee contacted to add more tickets. Use the second method addTicket to add the ticket

attendee2.addTicket() # calling that method adds one ticket
#attendee2.addTicket() # call it again to add the second ticket 

