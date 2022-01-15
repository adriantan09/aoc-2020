def validator1(passport):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    field_count = 0
    for field in fields:
        if field in passport:
            field_count += 1

    return field_count == 7