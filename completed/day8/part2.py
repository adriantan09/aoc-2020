from part1 import find_acc_before_infinite
from part1 import handle_step

def change_instructions(instructions):
    i, acc = 0, 0
    while i < len(instructions):
        instructions = switch_nop_jmp(instructions, i)

        # this case can be aggregated into one function
        if (not is_infinite_loop(instructions)):
            return find_acc_before_infinite(instructions)
        
        instructions = switch_nop_jmp(instructions, i)

        i, acc = handle_step(instructions, i, acc)

    return 0

def is_infinite_loop(instructions):
    i, acc = 0, 0
    visited_indicies = []
    while i < len(instructions):
        # infinite loop case
        if (i in visited_indicies):
            return True
        
        visited_indicies.append(i)

        i, acc = handle_step(instructions, i, acc)

    return False

def switch_nop_jmp(instructions, i):
    if (instructions[i][0] == 'nop'):
        instructions[i][0] = 'jmp'
    elif (instructions[i][0] == 'jmp'):
        instructions[i][0] = 'nop'
    return instructions

