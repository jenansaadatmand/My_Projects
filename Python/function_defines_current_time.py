# If we need to get the current date and time, you can use the datetime class of the datetime module. 
# Use datetime.now() to get the current date and time. 
# Then, use strftime() to create a string representing date and time in another format.

from datetime import datetime # module, class
def time():
    now = datetime.now() # function 
    return now.strftime("%D %A %H %M")

time()
print("Current time:", time())
print()