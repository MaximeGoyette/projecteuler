import datetime
date = datetime.datetime(1901,1,1)
n = 0
while date <= datetime.datetime(2000, 12, 30):
    if date.day == 1 and date.weekday()==6:
        n += 1
    date += datetime.timedelta(days=1)

print n