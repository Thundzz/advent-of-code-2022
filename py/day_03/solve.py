import argparse
import string
from functools import lru_cache, reduce
import itertools

def parse_line(line):
    n = len(line)
    left, right = line[:n//2], line[n//2:]
    return (left, right)

def parse_input(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()
        return [parse_line(l.strip()) for l in lines]

@lru_cache
def get_priority_map():
    low = zip(string.ascii_lowercase, range(1, 27))
    up = zip(string.ascii_uppercase, range(27, 53))
    return dict(list(low) + list(up))

def priority(item_type):
    return get_priority_map()[item_type]

def get_common(left, right):
    common = set(left) & set(right)
    assert len(common) == 1, f"Found {len(common)} common elements instead of 1"
    for element in common:
        return element

def find_priority_sum(rucksacks):
    return sum([
        priority(get_common(l, r))
        for l, r in rucksacks
    ])

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def extract(s):
    for e in s:
        return e

def solve_elf_groups(rucksacks):
    priorities = get_priority_map()
    item_types = priorities.keys()
    unique_items_by_elf = [ frozenset(l + r) for l, r in rucksacks ]
    s = 0
    for group in chunks(unique_items_by_elf, 3):
        common = reduce(lambda x, y: x & y, group)
        print(common)
        c = extract(common)
        s += priority(c)
    return s

def main(input_file):
    rucksacks = parse_input(input_file)
    ps = find_priority_sum(rucksacks)
    print(ps)
    s = solve_elf_groups(rucksacks)
    print(s)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=False, default="test.in")
    args = parser.parse_args()
    main(args.input)
