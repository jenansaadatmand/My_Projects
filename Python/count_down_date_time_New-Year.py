# Manipulating date and time object data, using a built-in datetime library in Python
# A date countdown program that calculates the next date when provided with the (years, months, weeks, and times) as input 
# pip install python-dateutil in terminal only once
# You can create date and time objects, loop through a range of dates, parse, and format date strings 
# Many uses of relativedelta to find out date count up, count down, and time remaining or to apply any datetime calculation


# Program calculates the number of dates and time remaining for New Year:
# Check this website for other uses of the python-dateutil package https://www.plus2net.com/python/date-relativedelta.php


from dateutil.relativedelta import relativedelta
from datetime import date
# Alternatively: you can import all package components by import *

dt = date.today()
print("Today:", dt)
print("No of days left for New Year")

dt2 = date(dt.year+1,1,1)
dt3 = relativedelta(dt2, dt)
print("Days:",dt3.days, " Months:", dt3.months, "Years:", dt3.years)
