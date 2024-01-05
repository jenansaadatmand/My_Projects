# A prime number is a whole number greater than 1 whose only factors are 1 and itself. 
# A factor is a whole number that can be divided evenly into another number. 
# The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.  
# Numbers that have more than two factors are called composite numbers.


# Code expressing for a defined function:

# A function defined to check if a number is prime:

def checkIfPrime (numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck%x == 0 ):
            return False
        return True

# Calling the function:

checkIfPrime(13)

# Assigning a variable to the function (uncomment the code below to activate it)
#answer = checkIfPrime(13)
#print(answer)
