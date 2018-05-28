import time

print("monotonic: \t\t", time.get_clock_info('monotonic'))
print("clock: \t\t\t", time.get_clock_info('clock'))
print("process time: \t", time.get_clock_info('process_time'))
print("perf counter: \t", time.get_clock_info('perf_counter'))
print("time: \t\t\t", time.get_clock_info('time'))