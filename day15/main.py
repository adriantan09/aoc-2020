import sys

from part1 import function1
from part2 import function2

assert len(sys.argv) == 2
numbers = open(sys.argv[1]).read().split(',')
numbers = [int(n) for n in numbers]

print('part 1:', function1(numbers))
# print('part 2:', function2(numbers))
