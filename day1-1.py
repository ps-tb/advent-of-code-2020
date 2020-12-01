import utilities

needed_total = 2020

lines = {int(x) for x in utilities.read_lines('day1.txt')}

for each in lines:
    complement = needed_total - each
    if complement in lines:
        print(complement * each)
        break

