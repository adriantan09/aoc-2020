import sys
import re

from part1 import validator1
from part2 import validator2

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().split('\n')

def validate_passwords(data, is_valid_password):
    n_valid_passwords = 0
    for line in data:
        start, end, letter, password = re.split('-|: | ', line)
        if (is_valid_password(start, end, letter, password)):
            n_valid_passwords += 1
    return n_valid_passwords

print('part 1:', validate_passwords(lines, validator1))
print('part 2:', validate_passwords(lines, validator2))