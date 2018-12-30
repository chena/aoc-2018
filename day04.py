from util import get_input
from collections import defaultdict
import datetime
import re

def process():
	logs = []
	guard_hrs = {}
	
	# sort the logs
	for log in get_input('day04.txt'):
		timestamp = datetime.datetime.strptime(log[1:17], '%Y-%m-%d %H:%M')
		content = 'sleep'
		pattern = re.compile('Guard #(.+) begins')
		found_guard = pattern.match(log[19:])
		if found_guard:
			content = found_guard.group(1)
			guard_hrs[content] = 0
		elif log.find('wake') > 0:
			content = 'wake'
		logs.append((timestamp, content))
	logs.sort(key=lambda log: log[0])

	# calculate total hours slept
	index = 0
	track_minutes = defaultdict(list)
	while index < len(logs):
		time, guard = logs[index]
		index += 1
		while index < len(logs) and logs[index][1] == 'sleep':
			sleep_time = logs[index][0]
			index += 1
			wake_time = logs[index][0]
			index += 1
			sleep_duration = (wake_time - sleep_time).seconds / 60
			for i in xrange(sleep_time.minute, sleep_time.minute + sleep_duration):
				track_minutes[i].append(guard)
			guard_hrs[guard] += sleep_duration
	# part1: find the guard that has the most minutes asleep and the max minute the max guard is alseep at
	max_guard = max(guard_hrs, key=guard_hrs.get)
	max_minute = max(map(lambda (k, v): (k, v.count(max_guard)), track_minutes.items()), key=lambda t: t[1])[0]
	# return max_minute * int(max_guard)

	# part2: find guard that is most frequently asleep on the same minute
	for m, guards in track_minutes.items():
		distinct_g = list(set(guards))
		counts = zip(distinct_g, [guards.count(g) for g in distinct_g])
		track_minutes[m] = max(counts, key=lambda c: c[1])
	max_guard_minute = max(track_minutes.items(), key=lambda (k, v): v[1])
	return max_guard_minute[0] * int(max_guard_minute[1][0])

print(process())


