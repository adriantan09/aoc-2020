from part1 import find_jolt_diff
from part2 import function2

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')
    lines = [int(n) for n in lines]

print('part 1:', find_jolt_diff(lines))
# print('part 2:', function2(lines))