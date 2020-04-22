# In Python, date, time and datetime classes provides a number of function to deal with dates, times and time intervals. Date and datetime are an object in Python, so when you manipulate them, you are actually manipulating objects and not string or timestamps. Whenever you manipulate dates or time, you need to import datetime function.

# The datetime classes in Python are categorized into main 5 classes.

# date – Manipulate just date ( Month, day, year)
# time – Time independent of the day (Hour, minute, second, microsecond)
# datetime – Combination of time and date (Month, day, year, hour, second, microsecond)
# timedelta— A duration of time used for manipulating dates
# tzinfo— An abstract class for dealing with time zones

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():
    # Date
    # today = date.today()
    # print("Today's date is", today)

    # the date's individual component
    # today = date.today()
    # print("Date Components:", today.day, today.month, today.year)

    # retrive today's weekday (0=Monday, 6=Sunday)
    # print("Today's weekday:", today.weekday())

    # Datetime
    # today = datetime.now()
    # t = datetime.time(datetime.now())
    # print("The current date and time is", t)

    # wd = date.weekday(today)
    # days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    # print("Today is day number %d" % wd)
    # print("which is a " + days[wd])


    # How to Format Date and Time Output with Strftime()
    now = datetime.now()
    print(now.strftime("%a, %d %B %Y"))

    # %C- indicates the local date and time, %x- indicates the local date, %X- indicates the local time
    print(now.strftime("%c"))
    print(now.strftime("%x"))
    print(now.strftime("%X"))

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - local's AM/PM
    print(now.strftime("%I:%M:%S %p")) # 12 hours:minute:second:AM
    print(now.strftime("%H:%M")) # 24 hours:minute

    # How to use Timedelta Objects
    print(timedelta(days=365, hours=8, minutes=15  ))
    print("today is: " + str(datetime.now()))
    print("one year from now it will be:" + str(datetime.now() + timedelta(days=365)))
    print("in one week and 4 days it will be " + str(datetime.now() + timedelta(weeks=1, days=4)))

    today = date.today()  # get todays date
    nyd = date(today.year, 1, 1)  # get New Year Day for the same year
    # use date comparison to see if New Year Day has already gone for this year
    # if it has, use the replace() function to get the date for next year
    if nyd < today:
        print ("New Year day is already went by %d days ago" % ((today - nyd).days))

if __name__ == "__main__":
    main()