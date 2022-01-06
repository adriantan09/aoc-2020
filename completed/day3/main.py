from part1 import count_trees
from part2 import traverse_slope

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')
    array = list(map(lambda x: list(x), lines))

print('part 1:', count_trees(array, 1, 3))
print('part 2:', traverse_slope(array))