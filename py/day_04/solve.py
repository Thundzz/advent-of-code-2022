import argparse
import string
from functools import lru_cache, reduce
import itertools

def parse_line(line):
    fst, snd = line.split(",")
    fmin, fmax = map(int, fst.split("-"))
    smin, smax = map(int, snd.split("-"))
    return (fmin, fmax), (smin, smax)


def parse_input(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()
        return [parse_line(l.strip()) for l in lines]

def overlaps(x1, y1, x2, y2):
    return x1 <= y2 and y1 >= x2

def is_contained(x1, y1, x2, y2):
    return (x1 <= x2 <=  y2 <= y1) or (x2 <= x1 <= y1 <= y2)

def count_overlaps(pairs, overlap_fn):
    x = [
        overlap_fn(x1, y1, x2, y2)
        for (x1, y1), (x2, y2) in pairs
    ]
    fully_contained = list(filter(lambda a:a, x))
    return len(fully_contained)



def main(file_name):
    pairs = parse_input(file_name)
    res = count_overlaps(pairs, is_contained)
    print(res)
    res = count_overlaps(pairs, overlaps)
    print(res)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=False, default="test.in")
    args = parser.parse_args()
    main(args.input)
