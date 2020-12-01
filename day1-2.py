import utilities

needed_total = 2020

def find_total(input):
    for index, each in enumerate(lines):
        for next_index, next_each in enumerate(lines, start=index+1):
            for next_next_index, next_next_each in enumerate(lines, start=next_index+1):
                if each + next_each + next_next_each == needed_total:
                    return each * next_each * next_next_each
    
    return none

lines = [int(x) for x in utilities.read_lines('day1.txt')]

print(find_total(lines))

