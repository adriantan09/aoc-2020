def validator2(start, end, letter, password):
    matches = 0
    if (password[int(start) - 1] == letter):
        matches += 1
    if (password[int(end) - 1] == letter):
        matches += 1
    return matches == 1