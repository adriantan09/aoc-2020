import re
from part1 import count_anyone_yes
from part2 import count_everyone_yes

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n\n')
    responses1 = list(line.replace('\n', '') for line in lines)
    responses2 = list(line.split('\n') for line in lines)

print('part 1:', count_anyone_yes(responses1))
print('part 2:', count_everyone_yes(responses2))