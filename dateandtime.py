import time

print('the epoch of time starts at '+time.strftime('%c',time.gmtime()))

print('The current timezone is {} with a offset of {}'.format(time.tzname[0], time.timezone))

if time.daylight!=0:
    print('\t daylight saving time is in effect in this location')
    print('\t the DST timezone is ' + time.tzname[1])
    
print('local time is '+ time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) 
print('UTC time is '+ time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime()))

import datetime
print(datetime.datetime.today())
print(datetime.datetime.now())
#code will be removed ignore utc.now |
print(datetime.datetime.utcnow())