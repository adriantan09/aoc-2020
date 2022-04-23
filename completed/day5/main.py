import sys

from part1 import find_max_seat_id
from part2 import find_seat_id

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().split('\n')

print('part 1:', find_max_seat_id(lines))
print('part 2:', find_seat_id(lines))