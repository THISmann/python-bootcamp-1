# import datetime

# today_date = datetime.date.today()
# actual_datetime = datetime.datetime.now()
# in_15_hours = actual_datetime + datetime.timdelta(hours=15, minutes=10)

# print(f"Today is the {today_date.strftime(" % d/%m")}")
# print(f"In 15 hours and 10 minutes it will be the {in_15_hours.strftime(" % d/%m")}")

# import math as m
# import os as system
# import time

# date = time.localtime()
# after = time.sleep(50)
# print(after)
# print(date.tm_min)
# print(m.e)
# print(dir(m))

import datetime

today_date = datetime.date.today()
actual_datetime = datetime.datetime.now()
in_15_hours = actual_datetime + datetime.timdelta(hours=15, minutes=10)

print(today_date)

#print(f"Today is the {today_date.day}/{today_date.month}")
# print(
#     f"In 15 hours and 10 minutes it will be the {in_15_hours.day}/{in_15_hours.month}")
