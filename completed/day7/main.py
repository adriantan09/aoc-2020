from part1 import count_bags_containing
from part2 import count_containing_bags

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')
    lines = [line.split(' contain ') for line in lines]

print('part 1:', count_bags_containing(lines))
print('part 2:', count_containing_bags(lines))