import datetime

time1 = datetime.time()
time2 = datetime.time(15, 30, 23)

print(type(time1), time1)
print(type(time2), time2)
print(time2.hour, time2.minute, time2.second)
