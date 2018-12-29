from util import get_input
from collections import defaultdict

def process():
    occupied_count = defaultdict(list)
    indices = set()
    for claim in get_input('day03.txt'):
        index = int(claim[1:claim.index('@')].strip())
        indices.add(index)
        start = claim.index('@') + 2
        pos, dim = claim[start:].split(': ')
        x, y = [int(i) for i in pos.split(',')]
        w, h = [int(i) for i in dim.split('x')]
        xx = range(x, x + w)
        yy = range(y, y + h)
        for i in xx:
            for j in yy:
                occupied_count[(i, j)].append(index)
    # part1
    # return sum([1 if len(v) > 1 else 0 for v in occupied_count.values()]) 
    # part 2
    blacklist = set()
    for values in occupied_count.values():
            if len(values) > 1:
                blacklist.update(values)
    return indices.difference(blacklist).pop()

print(process())
