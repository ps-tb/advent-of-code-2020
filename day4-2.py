import utilities
import re

optional_fields = {'cid'}
required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
byr = re.compile(r'^(19[2-9][0-9]|200[0-2])$')
iyr = re.compile(r'^(201[0-9]|2020)$')
eyr = re.compile(r'^(202[0-9]|2030)$')
hgt = re.compile(r'^(1([5-8][0-9]|9[0-3])cm)|(([5-6][0-9]|7[0-6])in)$')
hcl = re.compile(r'^#[0-9a-f]{6}$')
ecl = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
pid = re.compile(r'^\d{9}$')


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
            key_value_split = kv.split(':')
            key = key_value_split[0]
            value = key_value_split[1].strip()

            if key == 'byr' and byr.search(value) is not None:
                keys.add('byr')
            elif key == 'iyr' and iyr.search(value) is not None:
                keys.add('iyr')
            elif key == 'eyr' and eyr.search(value) is not None:
                keys.add('eyr')
            elif key == 'hgt' and hgt.search(value) is not None:
                keys.add('hgt')
            elif key == 'hcl' and hcl.search(value) is not None:
                keys.add('hcl')
            elif key == 'ecl' and ecl.search(value) is not None:
                keys.add('ecl')
            elif key == 'pid' and pid.search(value) is not None:
                keys.add('pid')

total_count += is_valid(keys)

print(total_count)
