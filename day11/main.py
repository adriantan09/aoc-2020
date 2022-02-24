from part1 import part1
from part2 import function2

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')
    seats = [list(l) for l in lines]

print('part 1:', part1(seats))
# print('part 2:', function2(lines))