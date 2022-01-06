from part1 import function1
from part2 import function2

with open('./example.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')

print('part 1:', function1(lines))
print('part 2:', function2(lines))