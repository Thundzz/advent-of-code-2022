def parse_input(input_file):
	with open(input_file, "r") as file:
		content = file.read()
		elves = content.strip().split("\n\n")
		return [map(int, elf.split("\n")) for elf in elves]

def main():
	elves = parse_input("input.txt")
	# elves = parse_input("test.in")
	calories = [sum(elf_calories) for elf_calories in elves]

	max_calories = max(calories)

	sorted_calories = sorted(calories)
	top_3 = sorted_calories[-3:]
	print(top_3)
	print(sum(top_3))


if __name__ == '__main__':
	main()