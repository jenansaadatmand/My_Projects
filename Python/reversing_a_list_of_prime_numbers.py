# Reversing a list
# There are two ways to reverse a list: 1. by reverse() method and 2. by a slicing operator 

# Method 1 via reverse() method:
# Syntax: list.reverse()

print("Method 1 via list.reverse() method:")

# Create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

print("This is a list of prime numbers:", prime_numbers)

# Reversing the list
prime_numbers.reverse()    # First you must reverse the list before printing it

print("Reversed list:", prime_numbers)  # Using the reverse() method
print()



# Another example:
# Operating System List:
systems = [
    'Windows',
    'MacOS',
    'Linux',
]
print("Operating System List: ", systems)
systems.reverse() # Reverses the original list permanently
print("Reversed list: ", systems)
print()
print(systems) # Print the original list again to confirm its changed
print()



# Method 2 via slicing operator:
print("Method 2 via slicing operator list[::-1]:")

# Operating Systems List
systems = ["Windows", "MacOS", "Linux"] 

print("Original List: ", systems)

# Reversing a list
# Syntax: reversed_list = systems[start:stop:step]

reversed_list = systems[::-1] # step back from last index

# updated list
print("Reversed_list: ", reversed_list)
print('Updated List:', systems) # to confirm original list changed
print()


# Accessing elements in reverse order using for loop and iteration over the elements within the list:
print("Accessing elements via a for loop iteration over the reversed list: ")

# Printing elements in Reversed Order using a for loop and iteration over elements within the reversed list
# Its better to use reversed() method to access individual elements a list in the reverse order

for o in reversed(systems): # Use o for the index
    print(o)



