import datetime

dt_now = datetime.datetime.now(datetime.timezone.utc)
print(dt_now)

print(dt_now.date())

print(dt_now.time())

dt = datetime.datetime.strptime("21/11/2006 16:30", "%d/%m/%Y %H:%M")
print(dt)

t_dalta = datetime.timedelta(days=1)

print(dt + t_dalta)