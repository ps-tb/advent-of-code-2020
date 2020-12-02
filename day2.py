import utilities
import re

# 1-3 a: abcde
def is_valid_part_1(input_dict):
    count = 0
    for each in input_dict['password']:
        if each == input_dict['letter']:
            count += 1
    
    if count >= int(input_dict['min']) and count <= int(input_dict['max']):
        return True
    
    return False

def is_valid_part_2(input_dict):
    password = input_dict['password']
    letter = input_dict['letter']
    if (password[int(input_dict['min']) - 1] == letter) ^ (password[int(input_dict['max']) - 1] == letter):
        return True
    
    return False

input = [x for x in utilities.read_lines("day2.txt")]
compiled_regex = re.compile(r'(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-zA-Z]): (?P<password>[a-zA-Z]+)')

valid_passwords = 0
for each in input:
    match = compiled_regex.match(each)
    if is_valid_part_2(match.groupdict()):
        valid_passwords += 1

print(valid_passwords)