# Functions:
# Define a basic function 
def func1(): # does not take any argument
    print("I am a function")

# Function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)    

# Function that returns a value
def cube(x):
    return x*x*x


# Function with default value for an argument
# A function that takes a number and raises it to the given power

def power(num, x=1): # function with an argument with default value 
    result = 1 
    for i in range(x):
        result = result * num
    return result




# Function with variable number of arguments 
# * character means: pass in a variable number of arguments


def multi_add(*args): # function with a variable number of arguments
    result = 0 # Define a variable that default to 0
    for x in args: # the function loops over each argument
        result = result + x # add them all to a running total
    return result  # Returns the resulted total

# you can combine a variable argument with a set argument, but always the variable argument must be at the end 




# Calling the functions: 
    
func1() # Calling the function 
print(func1()) # function still called within the print() function. Since the func1 does not return a value, python evaluates that as None, and prints the string representation of that.
print()
print()

print(func1) # The function is not executed at all since we are not including the parenthesis func1(). printing the value of the funciton iteself, which evaluates to this string that you see <function func1 at 0x10731ce00>, functions themselves are objects that can be passed around to other pieces of python code    
print()


func2(10, 20)
print(func2(10, 20)) # no return value from func2, so we print None
cube(3) # calling cube will print None, because it has a return and no print() statement
print(cube(3)) # print() function will print the return value of cube()which is 27

print()

power(2) # its a function that returns something and does not print on screen, so nothing happens
print(power(2)) # printing the return form the called function, 2 to the power of 1 = 2
print(power(2, 3)) # printing the return from the called function, 2 to the power of 3 = 8 (2*2*2)
print()
print(power(num=2, x=3)) 
print(power(x=3, num=2)) # Reversing order of arguments if you provide the named parameter as well along with the values
print()

print(multi_add(4, 5, 10, 4)) # variable arguments because *args variable parameters is defined in the function
print(multi_add(10, 4, 5, 10, 4)) # add 10 another argument