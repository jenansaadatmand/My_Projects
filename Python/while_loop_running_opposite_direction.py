# A while loop that runs the opposite direction, negative numbers, semantic error, logical error with no message indicating the error
# This loop was supposed to count down from 10, print earch number to the terminal untili t hits 0 and stop

i = 10 # setting the counter at 10, since 10 is not less than 0, the statement in the loop is never executed, nothing will be printed 
while i < 0:
    i -= 1 # decrement by 1
    print(i) 


# We want the while loop to run as long as i is greated than 0
i = 10 # here the counter starts at 10 and its greater than 0, so the while loop is executed, will print from 9 to 0, not including 10

while i > 0:
    i -= 1 
    print(i)
