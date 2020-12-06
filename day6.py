import utilities

def part_1():
    total_yeses = 0
    yeses = set()
    for line in utilities.read_lines('day6.txt'):
        if line == '\n':
            total_yeses += len(yeses)
            yeses = set()
        else:
            for char in line.strip():
                yeses.add(char)

    total_yeses += len(yeses)
    
    return total_yeses

def part_2():
    total_yeses = 0
    group_size = 0
    yeses = {k:0 for k in map(chr, range(97, 123))}

    for line in utilities.read_lines('day6.txt'):
        if line == '\n':
            for k,v in yeses.items():
                if v == group_size:
                    total_yeses += 1
            yeses = {k:0 for k in map(chr, range(97, 123))}
            group_size = 0
        else:
            group_size += 1
            for char in line.strip():
                yeses[char] += 1

    for k,v in yeses.items():
        if v == group_size:
            total_yeses += 1
    
    return total_yeses

print(part_2())