import re
from part1 import validator1
from part2 import validator2

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines = content.split('\n')

# Time complexity: O(n)
# where n is the number of lines in the input file
def validate_passwords(data, is_valid_password):
    n_valid_passwords = 0
    for line in data:
        start, end, letter, password = re.split('-|: | ', line)
        if (is_valid_password(start, end, letter, password)):
            n_valid_passwords += 1
    return n_valid_passwords

print('part 1:', validate_passwords(lines, validator1))
print('part 2:', validate_passwords(lines, validator2))