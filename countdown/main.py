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

'''
lanka_time = today + timedelta(hours=3.5)
print(f"Time Now in Sri Lanka: {lanka_time.hour}:{lanka_time.minute}")