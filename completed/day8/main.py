import sys

from part1 import find_accumlated_value
from part2 import change_instructions

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().split('\n')
lines = [[line.split(' ')[0], int(line.split(' ')[1])] for line in lines]

print('part 1:', find_accumlated_value(lines)['acc'])
print('part 2:', change_instructions(lines))