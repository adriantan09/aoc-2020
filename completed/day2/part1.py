def validator1(start, end, letter, password):
    occurrences = password.count(letter)
    return occurrences >= int(start) and occurrences <= int(end)