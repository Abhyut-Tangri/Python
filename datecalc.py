import time

#print(time.gmtime(0))
#print(time.localtime())
#print(time.time())

from time import monotonic as my_timer
import random

input('press enter to start')
wait_time=random.randint(1,6)
time.sleep(wait_time)
start_time=my_timer()
input('press enter to stop')
end_time=my_timer()
print('started at '+time.strftime('%X',time.localtime(start_time)))
print('ended at '+time.strftime('%X',time.localtime(end_time)))

print('your reaction time was {}'.format(end_time-start_time))

x=time.monotonic()
print('time():{}'.format(time.get_clock_info('time')))
print('perf_counter():{}'.format(time.get_clock_info('perf_counter')))
print('monotonic():{}'.format(time.get_clock_info('monotonic')))
print('process_time():{}'.format(time.get_clock_info('process_time')))
