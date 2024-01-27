from datetime import datetime, date, timedelta

def countdown(year,month,day):
    today = date.today()
    target_date = date(year,month,day)
    countdown = target_date - today
    countdown_str = str(abs(countdown))
    countdown_str = countdown_str.split(",",1)
    if countdown.days < 0:
        return f"was {countdown_str[0]} ago!"
    else:
        return f"{countdown_str[0]} to go!"

def countdown_workdays(year,month,day):
    """ Starts counting inclusive of today """
    today = datetime.today()
    target_date = datetime(year,month,day)
    weekday_counter = 1
    for i in range((target_date-today).days):
        weekday_checker = today + timedelta(days=i)
        if weekday_checker.isoweekday() < 6:
            weekday_counter += 1
    if weekday_counter != 1:
        return f"need to work {weekday_counter} more days..."
    elif weekday_counter == 1:
        return f"need to work {weekday_counter} more day!"

print(countdown(2023,12,12))
print(countdown_workdays(2023,12,12))


'''
To-Do's: 
# workday counter in the past!? 
# counting down only weekdays
# birthday calculator omitting the year
# simple timezone conversion Sri Lanka
    lanka_time = today + timedelta(hours=3.5)
    print(f"Time Now in Sri Lanka: {lanka_time.hour}:{lanka_time.minute}")

'''