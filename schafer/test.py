import datetime
import pytz

dt_str = 'January 15, 2024'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')   # 2nd argument tells python what format it's in
print(dt)