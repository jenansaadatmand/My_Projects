# Test cases: Commands or scripts designed to test a specific scenario


def check_temp(temp):
    if  temp < 15:
        print('Bring a jacket')
    elif temp > 25 and temp <= 35:
        print('Pack a jacket')
    elif temp > 35:
        print('Leave the jacket at home')

# Test the case by recalling the function itself with different values that fall within the range of each conditional statement to test them
        # I don't want to leave a jacket at home for a temperature below 15
print()

check_temp(10) # Excutes the first condition and stop
check_temp(30) # Execute the second condition and stop
check_temp(37) # Execute the third condition 
