# Functions:

# Define a basic function 

def func1(): # Doesn't take any argument
    print("I am a function")

# Function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)    

# Function that returns a value
def cube(x):
    return x*x*x


# Function with the default value for an argument
# A function that takes a number and raises it to the given power

def power(num, x=1): # Function with an argument with default value 
    result = 1 
    for i in range(x):
        result = result * num
    return result




# Function with a variable number of arguments 

# * character means: pass in a variable number of arguments


def multi_add(*args): # Function with a variable number of arguments
    result = 0 # Define a variable that defaults to 0
    for x in args: # The function loops over each argument
        result = result + x # Add them all to a running total
    return result  # Returns the resulted total

# You can combine a variable argument with a set argument, but always the variable argument must be at the end 




# Calling the functions: 
    
func1() # Calling the function 
print(func1()) # Function still called within the print() function. Since the func1 does not return a value, python evaluates that as None, and prints the string representation of that.
print()
print()

print(func1) # The function is not executed at all since we don't include the parenthesis func1(). printing the value of the function itself, which evaluates to this string that you see <function func1 at 0x10731ce00>, functions themselves are objects that can be passed around to other pieces of Python code    
print()


func2(10, 20)
print(func2(10, 20)) # No return value from func2, so we print None
cube(3) # Calling cube will print None because it has a return and no print() statement
print(cube(3)) # print() function will print the return value of cube()which is 27

print()

power(2) # It's a function that returns something and does not print on the screen, so nothing happens
print(power(2)) # Printing the return form the called function, 2 to the power of 1 = 2
print(power(2, 3)) # Printing the return from the called function, 2 to the power of 3 = 8 (2*2*2)
print()
print(power(num=2, x=3)) 
print(power(x=3, num=2)) # Reversing order of arguments if you provide the named parameter as well along with the values
print()

print(multi_add(4, 5, 10, 4)) # Variable arguments because *args variable parameters is defined in the function
print(multi_add(10, 4, 5, 10, 4)) # Add 10 another argument
