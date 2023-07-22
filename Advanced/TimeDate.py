# import time

# def send_emails():
#   for i in range(10000):
#     pass

# start = time.time()
# send_emails()
# end = time.time()
# duration = end - start
# print(duration)

from datetime import datetime, timedelta
import time

# dt = datetime(2018, 1, 1)
# dt = datetime.now() # Returns current datetime
# dt = datetime.strptime("2018/01/01", "%Y/%m/%d")#converts datetime strings 
# dt = datetime.fromtimestamp(time.time())

# print(f"{dt.year}/{dt.month}")
# print(dt.strftime("%Y/%m")) # converts a daytime object into a string

dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
print(dt1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total_seconds", duration.total_seconds())












