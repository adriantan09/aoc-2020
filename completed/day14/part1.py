import re

def function1(instructions):
    memory = {}
    mask = 0
    address = 0
    value = 0
    for instruction in instructions:
        if 'mask' in instruction:
            mask = instruction[7:]
        if 'mem' in instruction:
            address = int(re.search('[(0-9)]+', instruction).group(0))
            value = int(re.search('(?<=] = )([0-9]+)', instruction).group(0))
            value = str(bin(value))[2:].zfill(36)
            result = value
            for i in range(36):
                if mask[i] != 'X':
                    result = result[:i] + mask[i] + result[i+1:]
            memory[address] = int(result, 2)
    return sum(memory.values())
    