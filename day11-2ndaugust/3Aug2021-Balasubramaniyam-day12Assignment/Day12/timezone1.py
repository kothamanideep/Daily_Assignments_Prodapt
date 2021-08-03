import pytz
from datetime import datetime

standrad_time=pytz.utc
time_zone=pytz.timezone("America/Mexico_City")
print(datetime.now(standrad_time))
print(datetime.now(time_zone).strftime("%Y : %m : %d - %H : %M : %S"))
time_zone=pytz.timezone("Antarctica/Macquarie")
print(datetime.now(time_zone).strftime("%Y : %m : %d - %H : %M : %S"))
time_zone=pytz.timezone("Asia/Qatar")
print(datetime.now(time_zone).strftime("%Y : %m : %d - %H : %M : %S"))

