from part1 import find_acc_before_infinite
from part2 import change_instructions

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')
    lines = [line.split(' ') for line in lines]
    lines = [[line[0], int(line[1])] for line in lines]

print('part 1:', find_acc_before_infinite(lines))
print('part 2:', change_instructions(lines))