from part1 import find_first_fail_two_sum
from part2 import function2

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')
    lines = [int(n) for n in lines]

print('part 1:', find_first_fail_two_sum(lines))
# print('part 2:', function2(lines))