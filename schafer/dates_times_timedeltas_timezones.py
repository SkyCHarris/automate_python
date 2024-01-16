
#! Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones

# It's not always obvious when we should use each

# Naive vs Aware datetimes
# Naive -> easier to work with
# Aware -> determine timezone, track daylight savings, etc.

import datetime

d = datetime.date(2016, 7, 24)
print(d)

# Get today's local date

tday = datetime.date.today()
print(tday)

# Get just year, month, or date

tday = datetime.date.today()
print(tday.year)

# Get day of the week. 2 ways:
# 1. .weekday
# 2. .isoweekday

tday = datetime.date.today()
print(tday.weekday())   # Monday 0 Sunday 6
print(tday.isoweekday())    # Monday 1 Sunday 7

# TimeDeltas
# Difference between 2 dates or times
# Useful for when we want to do operations on our dates/times

tday = datetime.date.today()

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)

# Add/Subtract date from date

tday = datetime.date.today()
bday = datetime.date(2024, 8, 7)

tdelta = datetime.timedelta(days=7)

till_bday = (bday - tday)
print(till_bday)

# Print total minutes/seconds/etc.

tday = datetime.date.today()
bday = datetime.date(2024, 8, 7)

tdelta = datetime.timedelta(days=7)

till_bday = (bday - tday)
print(till_bday.total_seconds())

# Time
# Hours, minutes, seconds, microseconds

t = datetime.time(9, 30, 45, 100000)
print(t)

# Print hrs, mins, secs, micros

t = datetime.time(9, 30, 45, 100000)
print(t.hour)

# Date and Time

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)

# Grab just date or time

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt.date())

# Alternative Constructors for datetime

dt_today = datetime.datetime.today()    # returns current local datetime with timezone of none
dt_now = datetime.datetime.now()    # gives option to pass in a timezone
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

# Timezones
# Timezone aware datetime using pytz

import datetime
import pytz

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)
# includes utc offset

# Get UTC time that's time aware
# 1. 

import datetime
import pytz

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

#2.

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

# Convert to my timezone
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

# Check/Print Timezones

for tz in pytz.all_timezones:
    print(tz)

# Make naive datetime timezone aware
    
dt_mtn = datetime.datetime.now()
print(dt_mtn)
# local time, not timezone aware

# Convert to US Eastern timezone

dt_mtn = datetime.datetime.now()
print(dt_mtn)

dt_east = dt_mtn.astimezone('US/Eastern')
# throws error, must be timezone aware

# Run timezone localize function
# .localize()

dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')

dt_mtn = mtn_tz.localize(dt_mtn)
print(dt_mtn)
# now timezone aware

# Display, Pass Around, Save
# iso
# https://docs.python.org/3/library/datetime.html#:~:text=strftime()%20and%20strptime()%20Format%20Codes%C2%B6

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

print(dt_mtn.isoformat())

# strftime()

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

print(dt_mtn.strftime('%B %d, %Y'))

# Convert str to datetime
# strptime

dt_str = 'January 15, 2024'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')   # 2nd argument tells python what format it's in
print(dt)

# strftime -> datetime to string
# strptime -> string to datetime