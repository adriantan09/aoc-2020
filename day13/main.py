from part1 import function1
from part2 import function2

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')
    departure_time = int(lines[0])
    bus_ids = list(filter(lambda id: id != 'x', lines[1].split(',')))
    bus_ids = [int(id) for id in bus_ids]

print('part 1:', function1(departure_time, bus_ids))
# print('part 2:', function2(lines))