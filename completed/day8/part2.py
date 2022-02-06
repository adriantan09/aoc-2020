from part1 import find_accumlated_value
from part1 import handle_step

def change_instructions(instructions):
    i, acc = 0, 0
    while i < len(instructions):
        instructions = switch_nop_jmp(instructions, i)

        v = find_accumlated_value(instructions)
        if (not v['is_infinite']):
            return v['acc']
        
        instructions = switch_nop_jmp(instructions, i)

        i, acc = handle_step(instructions, i, acc)

    return -1

def switch_nop_jmp(instructions, i):
    if (instructions[i][0] == 'nop'):
        instructions[i][0] = 'jmp'
    elif (instructions[i][0] == 'jmp'):
        instructions[i][0] = 'nop'
    return instructions

