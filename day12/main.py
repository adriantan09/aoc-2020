from part1 import find_manhattan_dist
from part2 import function2

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')
    lines = [[l[0], int(l[1:])] for l in lines]

print('part 1:', find_manhattan_dist(lines))
# print('part 2:', function2(lines))