from part1 import find_2020_2sum
from part2 import find_2020_3sum

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')
    numbers = list(map(lambda n: int(n), lines))

print('part 1:', find_2020_2sum(numbers))
print('part 2:', find_2020_3sum(numbers))