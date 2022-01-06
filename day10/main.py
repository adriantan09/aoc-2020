from part1 import function1
from part2 import function2

f = open('./example.txt', 'r').read().split('\n')
data = f

print('part 1:', function1(data))
print('part 2:', function1(data))