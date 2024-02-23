# Function with variable number of arguments
# * character denotes variable arguments (args)

def multi_add(*args): # function with a variable number of arguments, *args means variable argumenrs
    result = 0 # Define a variable that default to 0
    for x in args: # the function loops over each argument, and stores the result in x index or item 
        result = result + x # add them all to a running total
    return result  # Returns the resulted total

print(multi_add(4, 5, 10, 4)) # variable arguments because *args variable parameters is defined in the function
print(multi_add(10, 4, 5, 10, 4))  # add 10 another argument

