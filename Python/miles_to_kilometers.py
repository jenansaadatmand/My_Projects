# A program that converts miles to kilometers

miles = input('Enter a distance in miles: ')
# kilometers_value = miles_value * 1.609344

# 1. Take the value entered by a User
# 2. Convert it to a value in kilometers
# 3. Print the result to the terminal 
# - Text description
# String concatenation 
# Use float() to convert the string to a float number with decimal points

# Soluton # 1:
miles_float = float(miles) # Convert string from input() to float() for calculations
kilometers = miles_float * 1.609344 # Convert miles to kilometers
print("That value in kilometers is")
print(kilometers)
print()


# Solution 2: 

miles_value = float(miles) # Convert string from input() to float() for calculations
kilometers_value = miles_value * 1.609344  # Convert miles to kilometers
print("The value in kilometers is", round(kilometers_value)) # rounding up the result using round()
print()

