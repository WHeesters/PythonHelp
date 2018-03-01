import sys

print(sys.version)
print("================================================")
print("DATETIME MODULE")
print("================================================")
import datetime

print("---------------------")
print("DATES")
print("---------------------")

some_date = datetime.date(2018, 7, 10)  # Gives given date in date object
date_today = datetime.date.today()  # Gives todays date in date object

print("The given date is: " + str(some_date))
print("The date of today is: " + str(date_today))
print("The current day is: " + str(date_today.day))  # Gives just the day on given date
print("The weekday is: " + str(date_today.weekday()))  # Gives the weekday on the given day (Monday = 0 Sunday = 6)
print("The isoweekday is: " + str(date_today.isoweekday()))  # Gives the isoweekday on the given day (Monday = 1 Sunday = 7)

tdelta = datetime.timedelta(days=7)  # Creates a timedelta

print("")
print("The date one week from now: " + str(date_today + tdelta))  # Gives the given date + a timedelta
print("The date one week ago: " + str(date_today - tdelta))  # Gives the given date - a timedelta

calc_tdelta = some_date - date_today  # Calculations with just dates gives a timedelta

print("Days until 2018-07-10: " + str(calc_tdelta.days))  # Gives just the amount of days
print("Total seconds until 2018-07-10: " + str(calc_tdelta.total_seconds()))  # Gives the total amount of seconds

print("")
print("")
print("---------------------")
print("TIMES")
print("---------------------")

some_time = datetime.time(9, 30, 45, 100000)  # Gives the given time in a time object

print("The given time is: " + str(some_time))
print("The given hour is: " + str(some_time.hour))  # Gives just the hour on the given time

print("")
print("")
print("---------------------")
print("DATETIMES")
print("---------------------")

some_datetime = datetime.datetime(2018, 7, 10, 9, 30, 45, 100000)  # Gives the given datetime in a datetime object

print("The given datetime is: " + str(some_datetime))
print("The given date is: " + str(some_datetime.date()))  # Gets just the date from a datetime object
print("The given time is: " + str(some_datetime.time()))  # Gets just the time from a datetime object
print("The given datetime + 7 days is: " + str(some_datetime + tdelta))  # Gives the given datetime + a timedelta

tdelta2 = datetime.timedelta(hours=12)

print("The given datetime + 12 hours is: " + str(some_datetime + tdelta2))  # Gives the given datetime + a timedelta

print("")
print("")
print("---------------------")
print("TIMEZONES")
print("---------------------")
import pytz

print("A list of all timezones (in pytz):")
for tz in pytz.all_timezones:
    print(tz)

today = datetime.datetime.today()  # Gives the current date and time as a datetime object without a timezone
now = datetime.datetime.now(pytz.timezone("Europe/Amsterdam"))  # Gives the current date and time as a datetime object with a given timezone
utcnow = datetime.datetime.utcnow()  # Gives the current utc date and time as a datetime object

print("")
print("The datetime of today: " + str(today))
print("The datetime of now (Europe/Amsterdam): " + str(now))
print("The datetime of utcnow: " + str(utcnow))

dt_hongkong = now.astimezone(pytz.timezone("Hongkong"))  # Gives a datetime object from a given datetime object and a timezone

print("The datetime of now (Hongkong): " + str(dt_hongkong))

dt_naive = datetime.datetime.now()
dt_tz = dt_naive.astimezone(pytz.timezone("Hongkong"))

print("Naive datetime object dt_naive: " + str(dt_naive))
print("dt_naive converted to a timezone aware dt_tz: " + str(dt_tz))

print("")
print("")
print("---------------------")
print("FORMATTING")
print("---------------------")

print("A date in isoformat: " + str(now.isoformat()))  # Converts a datetime object to isoformat
print("A date in mmm dd, yyyy format: " + str(now.strftime("%B %d, %Y")))  # Convert a datetime object to a string (https://docs.python.org/3.6/library/datetime.html#strftime-and-strptime-behavior)

dt_str = "March 01, 2018"
dt_dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")  # Converts a string to a datetime object

print("The string 'March 01, 2018' converted to a datetime object: " + str(dt_dt))
