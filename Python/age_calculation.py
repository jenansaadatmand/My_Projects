# Age Calculation: Program to calculate Age
# Input dates of birth in year, month, day format.
# output saying year month and days

from datetime import date
from dateutil.relativedelta import relativedelta
dt = date.today()
dob = date(1974,8,21) # dob = date of birth, date of birth as year, month, day
dt3 = relativedelta(dt,dob)
print("Years",dt3.years, "Months:", dt3.months, "days:", dt3.days)


