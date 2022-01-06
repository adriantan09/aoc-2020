# Time complexity: 
def scanner(passports):
    valid_passports = 0
    for passport in passports:
        if is_valid_passport(passport):
            valid_passports += 1

    return valid_passports

def is_valid_passport(passport):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    field_count = 0
    for field in fields:
        if field in passport:
            field_count += 1

    return field_count == 7