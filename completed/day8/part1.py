def find_accumlated_value(instructions):
    i, acc = 0, 0
    visited_indicies = []
    while i < len(instructions):
        # infinite loop case
        if (i in visited_indicies):
            return {'acc': acc, 'is_infinite': True}
        
        visited_indicies.append(i)

        i, acc = handle_step(instructions, i, acc)

    return {'acc': acc, 'is_infinite': False}

def handle_step(instructions, i, acc):
    if (instructions[i][0] == 'acc'):
        acc += instructions[i][1]
        i += 1
    elif (instructions[i][0] == 'jmp'):
        i += instructions[i][1]
    else:
        i += 1
    
    return i, acc