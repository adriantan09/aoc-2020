import sys
import re

from part1 import function1
from part2 import function2

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().split('\n\n')

rules = [int(n) for n in re.findall('[0-9]+', lines[0])]
your_ticket = [int(n) for n in re.findall('[0-9]+', lines[1])]
nearby_tickets = [int(n) for n in re.findall('[0-9]+', lines[2])]

# print(rules)
# print(your_ticket)
# print(nearby_tickets)

print('part 1:', function1(rules, nearby_tickets))
# print('part 2:', function2(lines))
