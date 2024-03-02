
def wash_car(amount_paid): # added a parameter to allow the function to change its behavior based on some input

    if (amount_paid == 12):  # platinum wash
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")

    if (amount_paid == 6):  # basic wash
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 

wash_car(12) # define the positional argument (values to the defined parameter), keep changing the positional argument to change the output behavior of the function  



print()

# Solution 2:
amount_paid = 12


def wash_car():
    if (amount_paid == 12):  # platinum wash
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")

    if (amount_paid == 6):  # basic wash
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 

wash_car()

