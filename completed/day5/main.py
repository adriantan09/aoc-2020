from part1 import find_max_seat_id
from part2 import find_seat_id

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')

print('part 1:', find_max_seat_id(lines))
print('part 2:', find_seat_id(lines))