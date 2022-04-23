def function2(numbers):
    numbers.sort()
    numbers.insert(0, 0)
    numbers.append(numbers[len(numbers) - 1] + 3)
    valid_removals = 0
    for i in range(1, len(numbers) - 1):
        copy = list(numbers)
        copy.remove(numbers[i])
        # print(copy)
        if valid_adapters(copy):
            # print(numbers[i])
            valid_removals += 1
    return 2 ** valid_removals

def valid_adapters(numbers):
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if diff > 3: return False
    
    return True