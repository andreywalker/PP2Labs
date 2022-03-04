
from datetime import datetime, timedelta
#1
today = datetime.now()
td = timedelta(5.0)
day5=today-td
print(day5)

#2

print(datetime.now())
td1=timedelta(1.0)
print(datetime.now()+td1)
print(datetime.now()-td1)

#3

print(datetime.now()-timedelta(0.0,0.0,datetime.now().microsecond))

#4

day1=datetime(2022,2,12,3,56,37,0)
day2=datetime(1984,5,11,7,5,6,0)
a=(day1-day2).total_seconds()
print(a)