# from datetime import datetime
# from datetime import timedelta

# from dateutil.relativedelta import *
# from dateutil import relativedelta

# ##Aug 7 1989 8:10 pm
# date_1 = datetime(1989, 8, 7, 20, 10)

# ##Dec 5 1990 5:20 am
# date_2 = datetime(1990, 12, 5, 5, 20)

# #This will find the difference between the two dates
# difference = relativedelta.relativedelta(date_2, date_1)

# years = difference.years
# months = difference.months
# days = difference.days
# hours = difference.hours
# minutes = difference.minutes

# print ("Difference is %s year, %s months, %s days, %s hours, %s minutes " %(years, months, days, hours, minutes))




# from datetime import timedelta
# from datetime import datetime

import datetime
from dateutil.parser import *
t1 = "2016-04-07T03:34:58Z"
t2 = "2016-04-07T03:31:18Z"
tt1 = parse(t1)
tt2 = parse(t2)
diff = tt1 - tt2

if (diff > datetime.timedelta(minutes=1)):
    print ("transaction outside the 60 sec window")
else:
    print ("transaction within the 60 sec window")


# if diff > 60:
# 	print("bigger than 60")
# else:
# 	print("within the window")


