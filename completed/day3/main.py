import sys

from part1 import count_trees
from part2 import traverse_slope

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().split('\n')
matrix = list(map(lambda x: list(x), lines))

print('part 1:', count_trees(matrix, 1, 3))
print('part 2:', traverse_slope(matrix))