from part1 import solution1
from part2 import function2

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')
    lines = [line.split(' contain ') for line in lines]

print('part 1:', solution1(lines))
# print('part 2:', function2(lines))