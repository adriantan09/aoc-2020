from part1 import count_trees
from part2 import traverse_slope

f = open('./input.txt', 'r').read().split('\n')
data = list(map(lambda x: list(x), f))

print('part 1:', count_trees(data, 1, 3))
print('part 2:', traverse_slope(data))