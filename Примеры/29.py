import datetime

date = datetime.datetime(2023, 1, 1)
now = datetime.datetime(2023, 1, 31)
delta = now - date

print(type(delta))
print(delta)
print(delta.days)
