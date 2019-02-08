from util import get_input

class Coordinate:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __hash__(self):
    return hash(self.x + self.y)

  def distance_from_to(self, other):
    return (other, self.distance_to(other))

  def distance_to(self, other):
    return sum([abs(self.x - other.x), abs(self.y - other.y)])

  def __str__(self):
    return '({}, {})'.format(self.x, self.y)
  
"""
find the size of the largest area
"""
def process_part1():  
  coord_areas = dict(zip(coordinates, [1]*len(coordinates)))
  for x in xrange(min_x, max_x+1):
    for y in xrange(min_y, max_y+1):
      c = Coordinate(x, y)
      if c not in coordinates:
        # check if coordinate creates infinite area
        if c.x in [min_x, max_y] or c.y in [min_y, max_y]:
          continue
        distances = [c.distance_from_to(t) for t in coordinates]
        # check if there are more than one coordinate equally far
        sorted_distanes = sorted([d[1] for d in distances])
        if (sorted_distanes[0] == sorted_distanes[1]):
          continue
        coord_areas[min(distances, key=lambda v: v[1])[0]] += 1
  print(max(coord_areas.values()))

"""
find the size of the region containing all locations with a total distance 
to all given coordinates of less than 10000
"""
def process_part2():
  region = 0
  for x in xrange(min_x, max_x+1):
    for y in xrange(min_y, max_y+1):
      c = Coordinate(x, y)
      total_distance = sum([c.distance_to(t) for t in coordinates])
      if total_distance < 10000:
        region += 1
  print(region)

# collect coordinates
coordinates = [Coordinate(int(p[0]), int(p[1])) for p in (line.split(', ') for line in get_input('day06.txt'))]
# find min/max x and y coordinates
xs = [c.x for c in coordinates]
ys = [c.y for c in coordinates]
min_x = min(xs)
max_x = max(xs)
min_y = min(ys)
max_y = max(ys)

# process_part1()
process_part2()
