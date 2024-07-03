import datetime
import pytz

# Get current local time (naive)
localtime = datetime.datetime.now()

# Convert local naive time to UTC naive time
utc_time = datetime.datetime.utcnow()

print('Naive local time {}'.format(localtime))
print('Naive UTC {}'.format(utc_time))

# Convert local naive time to aware local time in California timezone
local_tz = pytz.timezone('America/Los_Angeles')
aware_local_time = local_tz.localize(localtime)

# Convert UTC naive time to aware UTC time
aware_utc = pytz.utc.localize(utc_time)

print('Aware local time {}, time zone {}'.format(aware_local_time, aware_local_time.tzinfo))
print('Aware UTC {}, time zone {}'.format(aware_utc, aware_utc.tzinfo))
