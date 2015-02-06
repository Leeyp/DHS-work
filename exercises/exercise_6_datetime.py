__author__ = 'dhs'

import datetime

current_date = datetime.date.today()

print("Today's date is ", current_date.strftime("%d-%m-%Y"))
print("Today's date is ", current_date.strftime("%d%m%y"))
print("Today's date is ", current_date.strftime("%y%m%d"))

print(current_date.strftime("%A %d %B %Y"))

print(current_date.strftime("%a %d %b %Y"))