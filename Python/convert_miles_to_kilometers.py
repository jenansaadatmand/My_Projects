# A program that converts miles to kilometres

miles = input('Enter a distance in miles: ')
# kilometers_value = miles_value * 1.609344

# 1. Take the value entered by a User
# 2. Convert it to a value in kilometres
# 3. Print the result to the terminal 
# - Text description
# String concatenation 
# Use float() to convert the string to a float number with decimal points

miles_value = float(miles) # Convert string from input() to float() for calculations
kilometers_value = miles_value * 1.609344  # Convert miles to kilometers
print("The number you have entered is converted from " + "Miles to kilometers:", kilometers_value)
