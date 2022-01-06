# Time complexity: O(n^2)
def find_2020_2sum(numbers):
    for n1 in numbers:
        for n2 in numbers:
            if (n1 + n2 == 2020):
                return n1 * n2