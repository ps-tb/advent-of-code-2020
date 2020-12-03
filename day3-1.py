import utilities

rise = 1
run = 3
current_position = [run, rise]
tree = '#'
trees_found = 0

grid = [x.strip() for x in utilities.read_lines("day3.txt")]
row_length = len(grid[0])

while current_position[1] < len(grid):
    if grid[current_position[1]][current_position[0]] == tree:
        trees_found += 1
    current_position[0] = (current_position[0] + run) % row_length
    current_position[1] += rise

print(trees_found)