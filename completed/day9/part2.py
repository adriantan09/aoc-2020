def decypher(numbers, invalid_number):
    contiguous_range = find_contiguous_range(numbers, invalid_number)
    return min(contiguous_range) + max(contiguous_range)

def find_contiguous_range(numbers, invalid_number):
    contiguous_range = []
    
    for start_index in range(len(numbers)):
        i = start_index
        total = 0
        while total < invalid_number:
            contiguous_range.append(numbers[i])
            total = sum(contiguous_range)
            i += 1

        if total == invalid_number:
            return contiguous_range
        contiguous_range.clear()

    return [None]
