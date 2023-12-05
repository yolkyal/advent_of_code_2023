from collections import namedtuple, defaultdict

NumberMapping = namedtuple('NumberMapping', 'line_number number_index number_length number_value')
symbols = ['*', '#', '+', '$', '-', '%', '&', '/', '@', '=']
size = 0

def get_adjacent_coords(nm):
	return [(row, col) 
	for row in [nm.line_number-1, nm.line_number, nm.line_number+1] 
	for col in range(nm.number_index-1, nm.number_index + nm.number_length + 1)
	if (row >= 0) and (col >= 0) and (row < size) and (col < size)]

with open(0) as f:
	grid = []
	number_mappings = []
	for line_number, line in enumerate(f):
		grid.append(list(line.strip()))	
		size = len(line)
		
		number = ''
		for i, c in enumerate(line.strip()):
			if c.isdigit():
				number += c
			else:
				if number:
					number_mappings.append(NumberMapping(line_number, i-len(number), len(number), int(number)))
					number = ''
		if number:
			number_mappings.append(NumberMapping(line_number, i-len(number), len(number), int(number)))
	
	gears = defaultdict(list)
	for nm in number_mappings:
		for row, col in get_adjacent_coords(nm):
			if grid[row][col] == '*':
				gears[(row, col)].append(nm.number_value)

	total = 0
	for gear_vals in gears.values():
		if len(gear_vals) == 2:
			total += gear_vals[0] * gear_vals[1]
	print(total)
