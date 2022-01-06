from part1 import find_2020_2sum
from part2 import find_2020_3sum

f = open('./input.txt', 'r').read().split('\n')
numbers = list(map(lambda n: int(n), f))

print('part 1:', find_2020_2sum(numbers))
print('part 2:', find_2020_3sum(numbers))