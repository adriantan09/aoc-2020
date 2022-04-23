import sys

from part1 import part1
from part2 import part2

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().split('\n')
seats = [list(l) for l in lines]

# print('part 1:', part1(seats))
print('part 2:', part2(seats))