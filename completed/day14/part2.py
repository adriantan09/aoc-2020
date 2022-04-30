import re

def function2(instructions):
    memory = {}
    mask = 0
    address = 0
    value = 0
    for instruction in instructions:
        if 'mask' in instruction:
            mask = instruction[7:]
        if 'mem' in instruction:
            address = int(re.search('[(0-9)]+', instruction).group(0))
            address = str(bin(address))[2:].zfill(36)
            value = int(re.search('(?<=] = )([0-9]+)', instruction).group(0))
            
            for i in range(36):
                if mask[i] == 'X':
                    address = address[:i] + 'X' + address[i+1:]
                else:
                    address =  address[:i] + str(int(address[i]) | int(mask[i])) + address[i+1:]
            
            binaries = output_binaries(address)
            for binary in binaries:
                memory[binary] = value

    return sum(memory.values())

def output_binaries(binary):
    if binary == '':
        return ['']
    
    binary_list = output_binaries(binary[1:])
    if binary[0] != 'X':
        return list(map(lambda x: binary[0] + x, binary_list))
    
    return list(map(lambda x: '1' + x, binary_list)) + list(map(lambda x: '0' + x, binary_list))
