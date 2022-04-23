def find_first_fail_two_sum(numbers, preamble):
    for i in range(preamble, len(numbers)):
        if not two_sum(numbers[i-preamble:i], numbers[i]):
            return numbers[i] 
    return -1

def two_sum(numbers, target):
    for i in numbers:
        for j in numbers:
            if i != j and i + j == target:
                return True    
    return False
