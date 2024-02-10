# Creating a function that calculates how many days it takes to reach a destination, given distance and a constant speed as multiple arguments: 
# destination = speed * hours
def days_to_complete(destination, speed):
    hours = destination/speed
    return hours/24

# use the distance from Earth to the Moon to calculate how many days it would take to get to the Moon at a speed limit of 75 miles per hour: distance to moon = 238855
print(round(days_to_complete(238855, 75)))  # use round() to round the answer
