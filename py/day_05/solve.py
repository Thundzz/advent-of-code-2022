import argparse
import re
import copy

def parse_line(l):
    pattern = r'move (\d+) from (\d+) to (\d+)'
    count, src, dest = re.match(pattern, l.strip()).groups()
    return (int(count), int(src), int(dest))

def parse_input(file_name):
    with open(file_name) as file:
        top, bottom = file.read().split("\n\n")
    diagram = list(reversed(top.split("\n")))
    nb_stacks = len(diagram)
    crate_indices = [idx for idx, char in enumerate(diagram[0]) if char != " " ]
    stacks = [[l[i] for l in diagram[1:] if l[i] != " "] for i in crate_indices]
    instructions = [parse_line(l) for l in bottom.strip().split("\n")]
    return stacks, instructions


def follow_instructions(stacks, instructions, should_reverse):
    stacks = copy.deepcopy(stacks)
    for (count, src, dest) in instructions:
        if should_reverse:
            extracted = reversed(stacks[src-1][-count:])
        else:
            extracted = stacks[src-1][-count:]
        stacks[dest-1].extend(extracted)
        stacks[src-1] = stacks[src-1][:-count]
    return stacks

def main(file_name):
    stacks, instructions = parse_input(file_name)
    resulting_stacks = follow_instructions(stacks, instructions, should_reverse=True)
    print("".join([s[-1] for s in resulting_stacks]))
    resulting_stacks = follow_instructions(stacks, instructions, should_reverse=False)
    print("".join([s[-1] for s in resulting_stacks]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=False, default="test.in")
    args = parser.parse_args()
    main(args.input)
