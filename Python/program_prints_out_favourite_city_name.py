# A program that prints out your favorite city name
# The program has a function named favorite_city
# favourite_city function has one parameter:name
# call favorite_city at least three times
# Output should include: "One of my favorite cities is"

# Print out the name of a favorite city

def favorite_city(name):
    print("One of my favorite cities is", name)

favorite_city("Santa Barbara, California")
favorite_city("Asheville, North Carolina")
favorite_city("Amsterdam, Netherlands")

print()

# Solution 2: 

name = "Santa Barbara, California"
name1 = "Asheville, North Carolina"
name2 = "Amsterdam, Netherlands"

# Change name, name1, or name2 to get different output

# To ask the user for input
#name = input("Enter your favorite city:") 

def favorite_city(name):
    print("One of my favorite cities is ", name)


favorite_city(name)
favorite_city(name1)
favorite_city(name2)


print()
