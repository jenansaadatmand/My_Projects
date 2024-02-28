import re  # Importing regular expressions (Regex) into Python

five_digit_zip = '98101'
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'

# write a regular expression, which will identify five digits in a row, which is the minimum for a US zip code
# Use the letter r to indicate that the string that follows may include backslashes that the compiler should ignore.
# Include regular expression in single quotes, then type back slash, d for digit, '\d{5}', denoting five occurrences for the preceding expression, the digit.

five_digit_expression = r'\d{5}' # Created a regular expression
print(re.search(five_digit_expression, five_digit_zip)) # Use the Regex pattern to compare to the string using the re.search method, takes two arguments, the Regex and the string to compare against it

print(re.search(five_digit_expression, nine_digit_zip))
print(re.search(five_digit_expression, phone_number))
