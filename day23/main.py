import sys

from part1 import function1
from part2 import function2

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().split('\n')

print('part 1:', function1(lines))
print('part 2:', function2(lines))
