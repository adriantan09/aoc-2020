def find_jolt_diff(numbers):
    jolt_diff = {1: 0, 2: 0, 3: 1}
    jolt_diff[numbers[0]] += 1 # starting jolt

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        jolt_diff[diff] += 1

    return jolt_diff[1] * jolt_diff[3]
