# A function that calculates the distance of a planet to earth
# A function that requires one argument to be passed to it

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else: # catch-all conditions
        return "unable to compute that destination" 
print(distance_from_earth("Moon"))
print()
print(distance_from_earth("Saturn"))
print()

