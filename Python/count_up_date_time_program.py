# Manipulating date and time object data, using a built-in datetime library and installing python-dateutil package in python
# A date count-up program that calculates the next date when provided with the (years, months, weeks, and times) as input 
# pip install python-dateutil in terminal only once
# You can create date and time objects, loop through a range of dates, parse, and format date strings 
# many uses of relativedelta to find out date count up, count down and time remaining or to apply any datetime calculation

from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(years=1, months=1, weeks=1, hour=10)
print(now)

print()

