import re
from part1 import validator1

def validator2(passport):
    if not validator1(passport): return False
    
    # (Birth Year) - four digits; at least 1920 and at most 2002.
    byr = int(passport[passport.index('byr') + 1])
    if (byr < 1920 or byr > 2002): return False

    # (Issue Year) - four digits; at least 2010 and at most 2020.
    iyr = int(passport[passport.index('iyr') + 1])
    if (iyr < 2010 or iyr > 2020): return False

    # (Expiration Year) - four digits; at least 2020 and at most 2030.
    eyr = int(passport[passport.index('eyr') + 1])
    if (eyr < 2020 or eyr > 2030): return False

    # (Height) - a number followed by either cm or in:
    hgt = passport[passport.index('hgt') + 1]
    if ('cm' in hgt):
        hgt = int(hgt.replace('cm', ''))
        # at least 150cm and at most 193cm.
        if (hgt < 150 or hgt > 193): return False
    elif ('in' in hgt):
        hgt = int(hgt.replace('in', ''))
        # at least 59in and at most 76in
        if (hgt < 59 or hgt > 76): return False
    else: 
        return False

    # a # followed by exactly six characters 0-9 or a-f.
    hcl = passport[passport.index('hcl') + 1]
    valid_hcl = bool(re.match('^#[0-9,a-f]{6}$', hcl))
    if not (valid_hcl): return False

    # exactly one of: amb blu brn gry grn hzl oth.
    ecl = passport[passport.index('ecl') + 1]
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if (ecl not in valid_ecl): return False

    # a nine-digit number, including leading zeroes.
    pid = passport[passport.index('pid') + 1]
    valid_pid = bool(re.match('^[0-9]{9}$', pid))
    if not (valid_pid): return False

    return True
