# To convert a Python time float to a UTC-based struct_time, Python time module has a function called gmtime()

import time, calendar
print(time.gmtime(0))

# Use this call to discover your system's epoch
print(time.gmtime())

# inverse for this function is inside the calendar module

print(time.gmtime())
print(calendar.timegm(time.gmtime))

