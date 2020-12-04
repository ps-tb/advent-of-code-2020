import utilities
import re

optional_fields = {'cid'}
required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
key_value_regex = re.compile(r'^(?P<key>(byr|iyr|eyr|hgt|hcl|ecl|pid)+):(?P<value>.+)$')

def is_valid(input_keys):
    if required_fields.issubset(keys):
        return 1
    
    return 0

total_count = 0
keys = set()
for each in utilities.read_lines('day4.txt'):
    if each == '\n':
        total_count += is_valid(keys)

        keys = set()
    else:
        split = each.split(' ')
        for kv in split:
            match = key_value_regex.match(kv.strip())
            if match is not None and 'key' in match.groupdict():
                keys.add(match.groupdict()['key'])
    
total_count += is_valid(keys)

print(total_count)
