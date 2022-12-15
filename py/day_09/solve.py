import argparse
from math import floor

def parse_line(line):
    direction, count = line.split()
    return direction, int(count)

def parse_input(file_name):
    with open(file_name) as file:
         return [ parse_line(l.strip()) for l in file.readlines()]

def is_vertical_or_horizontal(diff):
    return abs(diff.real) == 2 or  abs(diff.imag) == 2

def steppify(v):
    nreal = floor(v.real/abs(v.real)) if v.real != 0 else 0
    nimg = floor(v.imag/abs(v.imag)) if v.imag != 0 else 0
    return complex(nreal, nimg)


def new_tail_position(head_pos, tail_pos):
    difference = head_pos - tail_pos
    distance = max(abs(difference.real), abs(difference.imag))
    if distance <= 1:
        return tail_pos
    else:
        return tail_pos + steppify(difference)


def simulate(instructions):
    head_position = complex(0,0)
    tail_position = complex(0,0)
    head_positions = [head_position]
    tail_positions = [tail_position]
    head_movements = {
        "R" : complex(1, 0),
        "L" : complex(-1, 0),
        "U" : complex(0, 1),
        "D" : complex(0, -1)
    }
    for direction, count in instructions:
        for _ in range(count):
            head_position += head_movements[direction]
            tail_position = new_tail_position(head_position, tail_position)
            head_positions.append(head_position)
            tail_positions.append(tail_position)

    return len(set(tail_positions))

def main(file_name):
    instructions = parse_input(file_name)
    # print(instructions)
    nb_tail_pos = simulate(instructions)
    print(nb_tail_pos)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=False, default="test.in")
    args = parser.parse_args()
    main(args.input)
