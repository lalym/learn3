from datetime import date, timedelta
dt = date(2000, 1, 1)
dt
datetime.date(2000, 1, 1)
delta = timedelta(days=1)
delta
datetime.timedelta(1)


from datetime import datetime
dt_now = datetime.now()
print(dt_now)

https://docs.python.org/3.5/library/datetime.html#strftime-and-strptime-behavior

Linux & Mac
>>> import locale
>>> locale.setlocale(locale.LC_TIME, "ru_RU")
>>> dt_now.strftime('%A %d %B %Y')
'суббота 01 октября 2016'
Windows
>>> import locale
>>> locale.setlocale(locale.LC_ALL, "russian")
>>> dt_now.strftime('%A %d %B %Y')
'суббота 01 октября 2016'

>>> date_string = '12/23/2010'
>>> date_dt = datetime.strptime(date_string, '%m/%d/%Y')
>>> date_dt
datetime.datetime(2010, 12, 23, 0, 0)