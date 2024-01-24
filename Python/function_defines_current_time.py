# If we need to get the current date and time, you can use the datetime class of the datetime module. 
# Use datetime.now() to get the current date and time. 
# Then, use strftime() to create a string representing date and time in another format.

from datetime import datetime # Module, Class
def time():
    now = datetime.now() # Function 
    return now.strftime("%D %A %H %M") # presenting time in Date, Day, Hour, Minute format

time()
print("Current time:", time())
print()
