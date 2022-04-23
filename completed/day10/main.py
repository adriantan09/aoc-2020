import sys

from part1 import find_jolt_diff
from part2 import function2

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().split('\n')
lines = [int(n) for n in lines]
lines.sort()

# print('part 1:', find_jolt_diff(lines))
print('part 2:', function2(lines))