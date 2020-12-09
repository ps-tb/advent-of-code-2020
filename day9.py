import utilities

numbers = [int(x) for x in utilities.read_lines('day9.txt')]

start = 25
sums = dict()
invalid = -1

for i in range(24, 0, -1):
    for j in range(i-1, -1, -1):
        summing = numbers[i] + numbers[j]
        if summing not in sums:
            sums[summing] = []
        sums[summing].append((i, j))

while start < len(numbers):
    current = numbers[start]
    if current not in sums:
        invalid = current
        break

    for i in range(start - 1, 0, -1):
        summing = numbers[start] + numbers[i]
        if summing not in sums:
            sums[summing] = []
        sums[summing].append((i, i-1))
    
    start += 1

print(invalid)

for i in range(len(numbers)):
    j = i + 1
    summing = numbers[i]
    while summing < invalid:
        summing += numbers[j]
        j += 1
    if summing == invalid:
        print(min(numbers[i:j+1]) + max(numbers[i:j+1]))
        break
    

