# Time complexity: O(n^3)
def find_2020_3sum(numbers):
    for n1 in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if (n1 + n2 + n3 == 2020):
                    return n1 * n2 * n3