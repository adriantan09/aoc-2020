import sys

from part1 import find_2020_2sum
from part2 import find_2020_3sum

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().split('\n')
numbers = list(map(lambda n: int(n), lines))

print('part 1:', find_2020_2sum(numbers))
print('part 2:', find_2020_3sum(numbers))