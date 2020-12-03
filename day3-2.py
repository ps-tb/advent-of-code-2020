import utilities
import math

TREE = '#'
SLOPES = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
GRID = [x.strip() for x in utilities.read_lines("day3.txt")]
ROW_LENGTH = len(GRID[0])

def calculate_trees(slope: tuple) -> int:
    current_position = [slope[1], slope[0]]
    trees_found = 0

    while current_position[1] < len(GRID):
        if GRID[current_position[1]][current_position[0]] == TREE:
            trees_found += 1
        current_position[0] = (current_position[0] + slope[1]) % ROW_LENGTH
        current_position[1] += slope[0]
    
    return trees_found

print(math.prod([calculate_trees(slope) for slope in SLOPES]))