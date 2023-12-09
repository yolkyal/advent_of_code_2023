def parse_game_round(s):
	xs = s.split(',')
	counts = {}
	for x in xs:
		c, v = x.split()
		counts[v] = int(c)
	return counts


def is_valid_game_round(game_round):
	counts = parse_game_round(game_round)
	return (counts.get('red', 0) <= 12) and (counts.get('green', 0) <= 13) and (counts.get('blue', 0) <= 14)


with open(0) as f:
	total = 0
	for line in f:
		line = line.strip().replace('Game ', '')
		game_number = int(line.partition(':')[0])
		game_rounds = line.partition(': ')[2].split(';')
		if all(is_valid_game_round(game_round) for game_round in game_rounds):
			total += game_number
	print(total)
