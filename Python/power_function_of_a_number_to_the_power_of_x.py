# A Power function that takes the number and returns the number after raisinf it with the given power 

# This is a function with default value for an argument
# This function that takes a number and raises it to the given power

def power(num, x = 1): # function with a default argument 
    result = 1 
    for i in range(x):
        result = result * num
    return result

print(power(2))
print(power(2, 3))

# What does i in range(x) mean?
# range() is a function that returns a list of numbers (in the range passed as argument) So when you write "for i in range(x)" you mean: "for each ITEM in LIST: do something" For each item in the list passed after the IN operator, code will run the next codes you wrote
# In Python, the "I" in "for I in range" is a variable that is used to store the value of the current iteration of a loop. The "I" variable can be named anything, but it is commonly used as a shorthand for "index". The "range" function in Python creates a sequence of numbers, which the "for" loop then iterates over
# if x = 3 , index/item in range(3): creates a sequence of numbers, and returns a list [0, 1, 2] excluding 3), which the for loop then iterates over, i is a variable used to store the value of the current iteration of the for loop
# Therefore, for [0, 1, 2], result is 1 * 2 = 2*2*2 = 8
