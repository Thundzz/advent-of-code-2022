import argparse

# @dataclass(init=True, repr=True)
# class Node:
#     node_type: str
#     children: list
#     value: int

def parse_input(file_name):
    with open(file_name) as file:
        lines = [ l.strip() for l in file.readlines()]
    stack = []
    current_folder = { "/" : {} }
    root = current_folder
    for line in lines:
        if "$ cd" in line:
            folder = line.split()[-1]
            if folder == "..":
                current_folder = stack.pop()
            else:
                stack.append(current_folder)
                current_folder = current_folder[folder]
        elif "$ ls" in line:
            continue
        else:
            fst, snd = line.split()
            if fst == "dir":
                current_folder[snd] = {}
            else:
                current_folder[snd] = int(fst)
    return root


def compute_total_sizes(tree, path, acc):
    if isinstance(tree, int):
        return tree
    else:
        s = 0
        for key, value in tree.items():
            fullpath = path + "/" +key
            ts = compute_total_sizes(value, fullpath, acc)
            if isinstance(value, dict):
                acc[fullpath] =  ts
            s += ts
        return s

def main(file_name):
    tree_structure = parse_input(file_name)
    # print(tree_structure)
    acc = {}
    compute_total_sizes(tree_structure, "", acc)
    ttl_small_files = sum([ size for path, size in acc.items() if size <= 100000])
    # print(acc)
    print(ttl_small_files)
    free_space = 70000000 - acc["//"]
    required = 30000000

    big_enough_dirs = [(path, size) for path, size in acc.items() if size >=  required - free_space ]
    # print(big_enough_dirs)
    smallest_dir_size = min([size for path, size in big_enough_dirs])
    print(smallest_dir_size)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=False, default="test.in")
    args = parser.parse_args()
    main(args.input)
