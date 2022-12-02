def parse_input(input_file):
	with open(input_file, "r") as file:
		lines = file.readlines()
		return [l.strip().split() for l in lines]


def score(move):
	return {
		"A": 1, "B": 2, "C": 3,
		"X": 1, "Y": 2, "Z": 3,
		"rock": 1, "paper": 2, "scissors": 3
	}[move]

def score_outcome(outcome):
	return {"w" : 6, "l": 0, "d": 3}[outcome]

def compute_outcome(rnd):
	opp, own = rnd
	mapping = {
		"X" : "rock", "Y": "paper", "Z": "scissors",
		"A" : "rock", "B": "paper", "C": "scissors"
	}
	oppf, ownf = mapping[opp], mapping[own]
	winning_configs = { ("paper", "scissors"), ("rock", "paper"), ("scissors", "rock") }
	if oppf == ownf:
		return "d"
	elif (oppf, ownf) in winning_configs:
		return "w"
	else:
		return "l"

def choose_move(opp, outcome):
	cycle = ["rock", "paper", "scissors"]
	mapping = {
		"A" : "rock", "B": "paper", "C": "scissors"
	}
	modifier = { "X" : -1, "Y" : 0, "Z" : 1 }
	choice = (cycle.index(mapping[opp]) + modifier[outcome]) % 3
	return cycle[choice]

def compute_score_round_simple(rnd):
	opp, own = rnd
	outcome = compute_outcome(rnd)
	return score(own) + score_outcome(outcome)

def compute_score_round_complex(rnd):
	opp, outcome = rnd
	outcome_mapped = { "X" : "l", "Y" : "d", "Z" : "w" }[outcome]
	own = choose_move(opp, outcome)
	return score(own) + score_outcome(outcome_mapped)


def compute_score(guide, compute_score_fn):
	return sum([
		compute_score_fn(round) for round in guide
	])



def main():
	strategy_guide = parse_input("input.txt")
	score = compute_score(strategy_guide, compute_score_round_simple)
	print(score)
	score = compute_score(strategy_guide, compute_score_round_complex)
	print(score)

if __name__ == '__main__':
	main()