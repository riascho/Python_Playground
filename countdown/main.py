from datetime import datetime, date, timedelta

today = datetime.now()
target_date = datetime(year=2023,month=9,day=4)
countdown = target_date - today #creates timedelta
countdown_days = countdown.days #extracts only the days from timedelta
print(f"{countdown_days} Days to go!")

mine = date(year=1990, month=2, day=18)
raja = date(year=1994, month=8, day=8)

today = date.today()

target_date = date(2023, 9, 20)

countdown = target_date - today
countdown = str(countdown)
countdown = countdown.split(",",1)

print(countdown[0])

'''
To-Do's: 
# birthday calculator omitting the year
# simple timezone conversion Sri Lanka

71 days, 23:56:07.156000 is a string representation of the timedelta object.

To get the days only, just get the, well, .days:

>>> from datetime import datetime
>>> 
>>> recordDate = datetime(year=2010, month=10, day=10)
>>> now = datetime.now()
>>> age = now - recordDate
>>> age  # age is the timedelta object
datetime.timedelta(2033, 61630, 853029)
>>> "%d days" % age.days
'2033 days'

'''
lanka_time = today + timedelta(hours=3.5)
print(f"Time Now in Sri Lanka: {lanka_time.hour}:{lanka_time.minute}")