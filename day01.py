"""
part 1: calculate total frequency from input
part 2: find the first repeating frequency 
"""
def _get_input():
	with open('input/day1.0.txt') as f:
		content = f.readlines()
	return content

def total_freq():
	return sum([int(v) for v in _get_input()])

def repeat_freq():
	data = _get_input()
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

# print total_freq()
print repeat_freq()
