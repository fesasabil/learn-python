# Calendar module in Python has the calendar class that allows the calculations for various task based on date, month, and year. On top of it, the TextCalendar and HTMLCalendar class in Python allows you to edit the calendar and use as per your requirement.

import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
# str = c.formatmonth(2020, 5)
# print(str)

for i in c.itermonthdays(2020, 5):
    print(i)

for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

for month in range (1,13):
    mycal = calendar.monthcalendar(2020, month)

    week1 = mycal[0]
    week2 = mycal[1]

    if week1[calendar.MONDAY] != 0:
        auditday = week1[calendar.MONDAY]
    else:
        auditday = week2[calendar.MONDAY]

    print("%10s %2d" % (calendar.month_name[month], auditday))