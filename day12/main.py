import sys

from part1 import find_manhattan_dist
from part2 import function2

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().split('\n')
lines = [[l[0], int(l[1:])] for l in lines]

print('part 1:', find_manhattan_dist(lines))
# print('part 2:', function2(lines))