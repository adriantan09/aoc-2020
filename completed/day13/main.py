import sys

from part1 import function1
from part2 import function2

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().split('\n')
departure_time = int(lines[0])
bus_ids = [int(id) for id in lines[1].split(',') if id.isdigit()]

print('part 1:', function1(departure_time, bus_ids))
print('part 2:', function2(lines[1].split(',')))