def function2(numbers):
    numbers.insert(0, 0)
    numbers.append(numbers[-1] + 3)
    return count_ways(numbers, 0)

def count_ways(numbers, i, cache={}):
    if i in cache:
        return cache[i]
    
    if i == len(numbers) - 1:
        return 1

    total = 0
    if i + 1 < len(numbers) and numbers[i + 1] - numbers[i] <= 3:
        total += count_ways(numbers, i + 1)

    if i + 2 < len(numbers) and numbers[i + 2] - numbers[i] <= 3:
        total += count_ways(numbers, i + 2)

    if i + 3 < len(numbers) and numbers[i + 3] - numbers[i] <= 3:
        total += count_ways(numbers, i + 3)

    cache[i] = total
    return total

