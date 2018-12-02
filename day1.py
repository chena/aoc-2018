"""
part 1: calculate total from input
"""
def _get_input():
	with open('input/day1.0.txt') as f:
		content = f.readlines()
	return content

def total_freq():
	content = _get_input()
	total = 0
	for val in content:
		op = val[0]
		num = int(val[1:])
		if op == '+':
			total += num
		else:
			total -= num
	return total

print total_freq()

