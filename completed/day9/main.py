import sys

from part1 import find_first_fail_two_sum
from part2 import decypher

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().split('\n')
lines = [int(n) for n in lines]

invalid_number = find_first_fail_two_sum(lines, 25)
print('part 1:', invalid_number)
print('part 2:', decypher(lines, invalid_number))