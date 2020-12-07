import utilities
import regex
from collections import namedtuple

EachBag = namedtuple('EachBag', ['amount', 'color'])
capture = regex.compile(r'(?P<top_bag>[a-z]+ [a-z]+) bags contain (?P<inner_bags>.*)')
bag = regex.compile(r'(?P<amount>\d)+ (?P<bag_type>[a-z ]+) bags?')

bag_contains = dict()
contained_by = dict()

for line in utilities.read_lines('day7.txt'):
    match = capture.match(line)
    groups = match.groupdict()
    top_bag = groups['top_bag']
    inner_bags = groups['inner_bags']

    if inner_bags != "no other bags.":
        inner_bags_match = [bag.match(x) for x in [x.strip().replace('.', '') for x in inner_bags.split(",")]]
        bag_contains[top_bag] = [EachBag(int(x['amount']), x['bag_type']) for x in inner_bags_match]
        for each in inner_bags_match:
            if each['bag_type'] not in contained_by:
                contained_by[each['bag_type']] = []
            contained_by[each['bag_type']].append(top_bag)

def find_bags_part_1(next_bag, all_bags):
    if next_bag in contained_by:
        for each in contained_by[next_bag]:
            all_bags.add(each)
            find_bags_part_1(each, all_bags)

total = set()
find_bags_part_1('shiny gold', total)
print(len(total))

def find_bags_part_2(key):
    total = 0

    if key not in bag_contains:
        return 0

    inner_bags = bag_contains[key]
    if len(inner_bags) == 0:
        return 0

    for each in inner_bags:
        total += each.amount + (each.amount * find_bags_part_2(each.color))

    return total

print(find_bags_part_2('shiny gold'))