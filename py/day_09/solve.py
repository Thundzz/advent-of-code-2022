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


def simulate(instructions, nb_knots):
    current_positions = [complex(0,0) for _ in range(nb_knots)]
    positions_history = [[complex(0,0)] for _ in range(nb_knots)]
    head_movements = {
        "R" : complex(1, 0),
        "L" : complex(-1, 0),
        "U" : complex(0, 1),
        "D" : complex(0, -1)
    }
    for direction, count in instructions:
        for _ in range(count):
            current_positions[0] += head_movements[direction]
            positions_history[0].append(current_positions[0])
            for i in range(1, nb_knots):
                current_positions[i] = new_tail_position(current_positions[i-1], current_positions[i])
                positions_history[i].append(current_positions[i])
    tail_positions = positions_history[-1]
    return len(set(tail_positions))

def main(file_name):
    instructions = parse_input(file_name)
    nb_tail_pos = simulate(instructions, 2)
    print(nb_tail_pos)
    nb_tail_pos = simulate(instructions, 10)
    print(nb_tail_pos)




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=False, default="test.in")
    args = parser.parse_args()
    main(args.input)
