import datetime as dt
from time import time
import pytz

'''dt1 = dt.datetime.now()
print(dt1)

dt2 = dt.datetime.now(pytz.utc)
print(dt2)

dt3 = dt.datetime.now(pytz.timezone("Europe/Berlin"))
print(dt3)'''

datetime_string = "2022-01-01 12:21:33"
datetime_NY =dt.datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")

current_timezone = pytz.timezone("US/Eastern")
target_timezone = pytz.timezone("Europe/Paris")

localized_NY = current_timezone.localize(datetime_NY)
datetime_Paris = localized_NY.astimezone(target_timezone)

print(datetime_Paris)
print(datetime_Paris.replace(tzinfo=None))
print(datetime_Paris.timetz())

#print(pytz.all_timezones)
#print(pytz.common_timezones)
print(pytz.country_timezones["PL"])
print(datetime_Paris.tzname())
