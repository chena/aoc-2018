import string

ALPHABETS = string.ascii_lowercase

def process(line):
  index = 0
  while index < len(line) - 1:
    one, two = line[index], line[index+1]
    if (one.upper() == two.upper() and one != two):
      del line[index:index+2]
      index -= 1
    else:
      index += 1
  return len(''.join(line).strip())

def scan():
  counts = []
  with open('input/day05.txt') as f:
    line =  f.readline()
  for a in ALPHABETS:
    to_process = filter(lambda c: c.lower() != a, list(line))
    counts.append(process(to_process))
  return(min(counts))

print(scan())



