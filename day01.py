from util import get_input

"""
part 1: calculate total frequency from input
part 2: find the first repeating frequency 
"""
def total_freq():
	return sum([int(v) for v in get_input('day01.txt')])

def repeat_freq():
	data = get_input('day01.txt')
	total = 0
	repeat_freq = None
	cache = {0}

	while repeat_freq is None:
		for val in data:
			total += int(val)
			if total in cache:
				repeat_freq = total
				break
			cache.add(total)
	return repeat_freq

print total_freq()
# print repeat_freq()
