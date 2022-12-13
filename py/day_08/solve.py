import argparse

def parse_input(file_name):
    with open(file_name) as file:
        # lines = [ l.strip() for l in file.readlines()]
        # file.read()




def main(file_name):
    _ = parse_input(file_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=False, default="test.in")
    args = parser.parse_args()
    main(args.input)
