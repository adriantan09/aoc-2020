from part1 import find_first_fail_two_sum
from part2 import decypher

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')
    lines = [int(n) for n in lines]

invalid_number = find_first_fail_two_sum(lines, 25)
print('part 1:', invalid_number)
print('part 2:', decypher(lines, invalid_number))