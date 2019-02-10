from util import get_input
from collections import defaultdict
import string

WORKER_COUNT = 5
EXTRA_WORK_TIME = 60
ALPHABETS = string.ascii_uppercase

def process_steps():
  while len(candidates) > 0:
    current = candidates.pop(0)
    steps.append(current)
    # check what goes after the current step
    next_candidates =  pre_parts[current]
    for c in next_candidates:
      # push candidate if it passes prerequisite
      if len(filter(lambda p: p in steps, post_parts[c])) == len(post_parts[c]):
        candidates.append(c)
    candidates.sort()
  return ''.join(steps)

def _calculate_time(step):
  return ALPHABETS.index(step) + EXTRA_WORK_TIME + 1

def _reduce_work(workers, work):
  for i in xrange(len(workers)):
    if workers[i] > 0:
      workers[i] -= 1
      if workers[i] == 0:
        # work is done for the step
        current = work[i]
        steps.append(current)
        # check next steps
        for c in pre_parts[current]:
          # push candidate if it passes prerequisite
          if all(p in steps for p in post_parts[c]):
            candidates.append(c)
        work[i] = None

def process_time():
  workers = [0] * WORKER_COUNT
  work = [None] * WORKER_COUNT
  current_time = 0

  while len(candidates) > 0 or any(w != 0 for w in workers):
    if any(w == 0 for w in workers):
      for i in xrange(len(workers)):
        if len(candidates) == 0:
          break
        if workers[i] > 0:
          continue
        current = candidates.pop(0)
        # pick worker and set work
        index = workers.index(0)
        workers[index] = _calculate_time(current)
        work[index] = current
    # calculate remaining work and increase time
    _reduce_work(workers, work)
    current_time += 1
    candidates.sort()
  return current_time

pre_parts = defaultdict(list)
post_parts = defaultdict(list)
lines = get_input('day07.txt')
steps = []

for line in lines:
  before = line[line.find(' must')-1]
  after = line[line.find(' can')-1]
  pre_parts[before].append(after)
  post_parts[after].append(before)

candidates = sorted(set(pre_parts.keys()) - set(post_parts.keys()))

# print(process_steps())
print(process_time())

