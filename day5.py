import utilities
import math

lower_row = 'F'
upper_row = 'B'
upper_column = 'R'
lower_column = 'L'

def find_row_bounds(input, current_row, lower, upper):
    if input[current_row] == lower_row:
        upper = math.floor(lower + ((upper - lower)/2))

        if current_row == 6:
            return upper

    if input[current_row] == upper_row:
        lower = math.ceil(lower + ((upper - lower)/2))

        if current_row == 6:
            return lower
    
    return find_row_bounds(input, current_row + 1, lower, upper)

def find_column_bounds(input, current_column, lower, upper):
    if input[current_column] == lower_column:
        upper = math.floor(lower + ((upper - lower)/2))

        if current_column == 9:
            return upper

    if input[current_column] == upper_column:
        lower = math.ceil(lower + ((upper - lower)/2))

        if current_column == 9:
            return lower
    
    return find_column_bounds(input, current_column + 1, lower, upper)

ids = []
for each in utilities.read_lines('day5.txt'):
    row = find_row_bounds(each, 0, 0, 127)
    column = find_column_bounds(each, 7, 0, 7)
    id = row * 8 + column
    ids.append(id)

ids.sort(reverse=True)
max_id = ids[0]
min_id = ids[len(ids)-1]
print(max_id)

for each in range(min_id, max_id + 1):
    if each not in ids:
        print(each) 
        break