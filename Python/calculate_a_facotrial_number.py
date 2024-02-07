# A program or a function that calculates a factorial of a number
# The factorial of a number is the product of all the integers from 1 to that number.

# For example, the factorial of 6 is 1*2*3*4*5*6 = 720. Factorial is not defined for negative numbers, and the factorial of zero is one, 0! = 1.


# A factorial: is a function that multiplies a number by every number below it till 1. 
# For example, the factorial of 3 represents the multiplication of numbers 3, 2, 1, i.e. 3! = 3 × 2 × 1 and is equal to 6.

def factorial(n):  # Defining a function 
    if n < 0:
        return "Error: n must be a non-negative integer"
    elif n==0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("The factorial of 7 is", factorial(7))



# A zero factorial is a mathematical expression for the number of ways to arrange a data set with no values in it, which equals one. In general, the factorial of a number is a shorthand way to write a multiplication expression wherein the number is multiplied by each number less than it but greater than zero. The factorial of zero is, symbolically represented as. = 1.

# The recursive call is with n-1, which ensures that the value of n decreases with each recursive call, and the function will eventually reach the base case.
print()



# Solution 2: to find factorial of a number that is provided by the user
# To test the program, change the value of num to get a different result
# The number whose factorial is to be found is stored in num, and we check if the number is negative, zero or positive using if...elif...else statement. If the number is positive, we use for loop and range() function to calculate the factorial.


num = 7

# To take input from the user
#num = int(input("enter a number: "))

factorial = 1
# Check if the number is negative, positive or zero

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)


#The program iteration	factorial*i (returned value)
# i = 1	    1 * 1 = 1
# i = 2	    1 * 2 = 2
# i = 3	    2 * 3 = 6
# i = 4	    6 * 4 = 24
# i = 5	    24 * 5 = 120
# i = 6	    120 * 6 = 720
# i = 7	    720 * 7 = 5040

print()


# Solution 3: Factorial of a Number using Recursion
# factorial() is a recursive function that calls itself. Here, the function will recursively call itself by decreasing the value of the x.

def factorial(x):
    """This is a recursive function to find the factorial of an integer"""

    if x == 1:
        return 1

    else:
        # recursive call to the function
        return (x * factorial(x-1))

# change the value for a different result
num = 7
# To take input from the User
# num = int(input("Enter a number: "))

# Call the factorial function
result = factorial(num)

print("The factorial of", num, "is", result)
