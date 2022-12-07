import argparse

def parse_input(file_name):
	with open(file_name) as file:
		return file.read().strip()

def find_start_of_packet(datastream, marker_size):
	for i in range(len(datastream)):
		word = datastream[i:i+marker_size]
		if len(set(datastream[i:i+marker_size])) == marker_size:
			print(word)
			return i + marker_size

def main(file_name):
	datastream = parse_input(file_name)
	idx = find_start_of_packet(datastream, 4)
	print(idx)
	idx = find_start_of_packet(datastream, 14)
	print(idx)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=False, default="test.in")
    args = parser.parse_args()
    main(args.input)
