import argparse
from functools import reduce
from operator import mul
import numpy as np

def parse_input(file_name):
    with open(file_name) as file:
        lines = [ [ int(c) for c in l.strip()] for l in file.readlines()]
    return np.matrix(lines)

def compute_visibility(trees):
    n, _ = trees.shape
    highest_lr = np.zeros(trees.shape)
    for i in range(n):
        maxi = trees[i, 0]
        for j in range(n):
            highest_lr[i, j] = maxi
            maxi = max(maxi, trees[i, j])
    highest_rl = np.zeros(trees.shape)
    for i in range(n):
        maxi = trees[i, n-1]
        for j in range(n-1, -1, -1):
            highest_rl[i, j] = maxi
            maxi = max(maxi, trees[i, j])
    highest_ud = np.zeros(trees.shape)
    for j in range(n):
        maxi = trees[0, j]
        for i in range(n):
            highest_ud[i, j] = maxi
            maxi = max(maxi, trees[i, j])
    highest_du = np.zeros(trees.shape)
    for j in range(n):
        maxi = trees[n-1, j]
        for i in range(n-1, -1, -1):
            highest_du[i, j] = maxi
            maxi = max(maxi, trees[i, j])
    is_visible = np.zeros(trees.shape)
    for i in range(n):
        for j in range(n):
            l =[
                 (trees[i, j] - highest_lr[i, j]),
                 (trees[i, j] - highest_rl[i, j]),
                 (trees[i, j] - highest_du[i, j]),
                 (trees[i, j] - highest_ud[i, j])
             ]
            is_visible[i, j] = max(l)
    xx  = (is_visible[1:-1, 1:-1] > 0).sum()
    return 4 * (n - 1) + xx

def compute_scenic_score(trees):
    n, _ = trees.shape
    scenic_scores = np.zeros(trees.shape)
    for i in range(1, n-1):
        for j in range(1, n-1):
            distances = []
            distance = 0
            for ii in range(i-1, -1, -1):
                distance += 1
                if trees[ii, j] >= trees[i, j]:
                    break
            distances.append(distance)
            distance = 0
            for ii in range(i+1, n):
                distance += 1
                if trees[ii, j] >= trees[i, j]:
                    break
            distances.append(distance)
            distance = 0
            for jj in range(j-1, -1, -1):
                distance += 1
                if trees[i, jj] >= trees[i, j]:
                    break
            distances.append(distance)
            distance = 0
            for jj in range(j +1, n):
                distance += 1
                if trees[i, jj] >= trees[i, j]:
                    break
            distances.append(distance)
            # print(i, j, distances)
            scenic_scores[i, j] = reduce(mul, distances)
    print(scenic_scores.max())



def main(file_name):
    trees = parse_input(file_name)
    # print(trees)
    nb_visible = compute_visibility(trees)
    print(nb_visible)
    scenic_scores = compute_scenic_score(trees)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=False, default="test.in")
    args = parser.parse_args()
    main(args.input)
