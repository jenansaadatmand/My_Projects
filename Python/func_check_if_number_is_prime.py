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
