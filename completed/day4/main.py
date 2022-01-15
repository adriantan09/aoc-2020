import re
from part1 import validator1
from part2 import validator2

with open('./input.txt', 'r') as fd:
    content = fd.read()
    lines  = content.split('\n\n')
    passports = list(line.replace('\n', ' ') for line in lines)
    passports = list(re.split(':| ', p) for p in passports)

# Time complexity: O(n)
# where n is the number of passports in the input file
def valid_passports(passports, is_valid_passport):
    valid_passports = 0
    for passport in passports:
        if is_valid_passport(passport):
            valid_passports += 1

    return valid_passports

print('part 1:', valid_passports(passports, validator1))
print('part 2:', valid_passports(passports, validator2))