from datetime import date
from datetime import datetime


day_now = date.today()
print(day_now)



xday = date(1980, 1, 1)
td = day_now - xday
print(td)


now = datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

dum_day = datetime(2019, 5, 1, hour=15, minute=15, second=15, microsecond=0)
print(dum_day)

dt_now = datetime.now()
print(dt_now)
