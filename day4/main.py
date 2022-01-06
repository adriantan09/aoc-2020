import re
from part1 import scanner
from part2 import function2

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines  = content.split('\n\n')
    passports = list(line.replace('\n', ' ') for line in lines)
    passports = list(re.split(':| ', p) for p in passports)

print('part 1:', scanner(passports))
# print('part 2:', function1(data))