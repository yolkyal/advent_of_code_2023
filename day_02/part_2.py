def parse_game_round(s):
	xs = s.split(',')
	counts = {}
	for x in xs:
		c, v = x.split()
		counts[v] = int(c)
	return counts


def get_maxes(game_rounds):
	maxes = {'red': 0, 'green': 0, 'blue': 0}
	for game_round in game_rounds:
		counts = parse_game_round(game_round)
		maxes['red'] = max(maxes['red'], counts.get('red', 0))
		maxes['green'] = max(maxes['green'], counts.get('green', 0))
		maxes['blue'] = max(maxes['blue'], counts.get('blue', 0))
	return maxes


with open(0) as f:
	total = 0
	for line in f:
		line = line.strip().replace('Game ', '')
		game_number = int(line.partition(':')[0])
		game_rounds = line.partition(': ')[2].split(';')
		maxes = get_maxes(game_rounds)
		total += maxes['red'] * maxes['green'] * maxes['blue']
	print(total)
