#Importing built-in modules containing functions. import random module
#import random
#to use randrange()
# random.randrange(1, 10)
#print(random.randrange(1, 10))
print()
#import random as r to abbreviate random each time you use it
#print(r.randrange(1, 10))
#a = r.randrange(1,100)
print()

#import specific function from module. randrange()
#random import randrange

#import more than one function,randrange(), randint(), to use function you don't need to use dot notation
from random import randrange, randint
print(randrange(1,10))
print(randint(1, 10))
print()

# Create your own module, save it as .py, and place in Python folder that you are going to import from 
#Importing created prime module and checkIfPrime() function from the same folder as new program
import prime #Importing module
prime.checkIfPrime(13) # Calling the function
answer = prime.checkIfPrime(13) # Assigning variable to returned expression from function
print(answer)
print()

# Importing module stored in a different folder than new program, import sys
