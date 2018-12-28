from util import get_input

def checksum():
	content = get_input('day02.txt')
	two = 0
	three = 0
	for line in content:
		counts = [line.count(l) for l in set(line.strip())]
		two += 1 if 2 in counts else 0
		three += 1 if 3 in counts else 0
	return two * three

def box_ids_letters():
	content = get_input('day02.txt')
	for first in content:
		for second in content:
			diff = 0 
			for i in xrange(len(first)):
				if first[i] != second[i]:
					diff += 1
				if diff > 1:
					continue
			if diff == 1:
				ans = ''
				for pair in zip(first, second):
					if pair[0] == pair[1]:
						ans += pair[0]
				return ans

# print(checksum())
print(box_ids_letters())