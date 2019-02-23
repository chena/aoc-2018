from util import get_input

class Node:
  def __init__(self, ccount, mcount):
    self.ccount = ccount
    self.mcount = mcount
    self.children = []
    self.metadata = []

  def add_child(self, n):
    self.children.append(n)

  def add_metadata(self, m):
    self.metadata.append(m)

  def get_value(self):
    if self.ccount == 0:
      return sum(self.metadata)
    return sum([0 if i > self.ccount else self.children[i - 1].get_value() for i in self.metadata])

  def __str__(self):
    return 'children_count: {}, metadata: {}'.format(self.ccount, self.metadata)

def process(node, total):
  ccount, mcount = node.ccount, node.mcount
  for _ in xrange(ccount):
    n = Node(metadata.pop(0), metadata.pop(0))
    process(n, total)
  for _ in xrange(mcount):
    total.append(metadata.pop(0))

def process_part2(node):
  ccount, mcount = node.ccount, node.mcount
  for _ in xrange(ccount):
    c = Node(metadata.pop(0), metadata.pop(0))
    node.add_child(c)
    process_part2(c)
  for _ in xrange(mcount):
    node.add_metadata(metadata.pop(0))

def print_tree(node):
  print(str(node))
  for c in node.children:
    print_tree(c)

metadata = [int(v) for v in get_input('day08.txt')[0].strip().split(' ')]
# create root
node = Node(metadata.pop(0), metadata.pop(0))

# part1
all_total = []
# process(node, all_total)
# print(sum(all_total))

# part2
process_part2(node)
print(node.get_value())
# print_tree(node)
