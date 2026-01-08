import datetime

date = datetime.date(2023, 2,1)
today = datetime.date.today()

time = datetime.time(12, 30 ,0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2026,1,2,12,30,1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("target date has passed")
else:
    print("target date has not passed")

print(date)
print(today)
print(time)
print(now)