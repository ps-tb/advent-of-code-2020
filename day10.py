import utilities

adapters = sorted([int(x.strip()) for x in utilities.read_lines('day10.txt')])
adapters.insert(0, 0)
adapters.append(adapters[-1] + 3)
differences = {k:0 for k in range(4)}
start = 0

for each in adapters:
    diff = each - start
    differences[diff] += 1
    start = each

print(differences[1]*differences[3])

ways = {k:0 for k in range(len(adapters))}
ways[0] = 1
for index in range(1, len(adapters)):
    prior_index = index - 1

    while prior_index >= 0 and (adapters[index]-adapters[prior_index] < 4):
        ways[index] += ways[prior_index]
        prior_index -= 1

print(ways[len(adapters)-1])


