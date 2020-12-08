import utilities
import copy

no_op = 'nop'
jump = 'jmp'
accumulate = 'acc'

input_instructions = [x.strip() for x in utilities.read_lines('day8.txt')]

def sum_registers(instructions):
    accumulated = 0
    current_instruction = 0 
    previous_instructions = set()

    while current_instruction not in previous_instructions:
        previous_instructions.add(current_instruction)

        if current_instruction >= len(instructions):
            break

        split = instructions[current_instruction].split()
        instruction = split[0]
        value = int(split[1])

        if instruction == no_op:
            current_instruction += 1
        elif instruction == jump:
            current_instruction += value
        else:
            current_instruction += 1
            accumulated += value
        
    return (accumulated, current_instruction)

# part 1
result = sum_registers(input_instructions)
print(result[0])

# part 2
to_change = 0

while result[1] != len(input_instructions):
    instructions_copy = copy.deepcopy(input_instructions)

    if instructions_copy[to_change].find(jump) != -1:
        instructions_copy[to_change] = instructions_copy[to_change].replace(jump, no_op)
    elif instructions_copy[to_change].find(no_op) != -1:
        instructions_copy[to_change] = instructions_copy[to_change].replace(no_op, jump)
    else:
        to_change += 1
        continue
    
    result = sum_registers(instructions_copy)

    to_change += 1

print(result[0])