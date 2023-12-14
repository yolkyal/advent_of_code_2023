def tilt_north(grid):
	for line_num in range(1, len(grid)):
		for line_index in range(len(grid[line_num])):
			if grid[line_num][line_index] == 'O':
				new_line_num = None
				for other_line_num in range(line_num-1, -1, -1):
					if grid[other_line_num][line_index] == '.':
						new_line_num = other_line_num
					else:
						break
				if new_line_num != None:
					grid[new_line_num][line_index] = 'O'
					grid[line_num][line_index] = '.'

def tilt_south(grid):
	for line_num in range(len(grid)-1, -1, -1):
		for line_index in range(len(grid[line_num])):
			if grid[line_num][line_index] == 'O':
				new_line_num = None
				for other_line_num in range(line_num + 1, len(grid)):
					if grid[other_line_num][line_index] == '.':
						new_line_num = other_line_num
					else:
						break
				if new_line_num != None:
					grid[new_line_num][line_index] = 'O'
					grid[line_num][line_index] = '.'

def tilt_west(grid):
	for line in grid:
		for i in range(len(line)):
			if line[i] == 'O':
				new_index = None
				for other_index in range(i-1, -1, -1):
					if line[other_index] == '.':
						new_index = other_index
					else:
						break
				if new_index != None:
					line[new_index] = 'O'
					line[i] = '.'

def tilt_east(grid):
	for line in grid:
		for i in range(len(line)-1, -1, -1):
			if line[i] == 'O':
				new_index = None
				for other_index in range(i+1, len(line)):
					if line[other_index] == '.':
						new_index = other_index
					else:
						break
				if new_index != None:
					line[new_index] = 'O'
					line[i] = '.'

def cycle(grid):
	tilt_north(grid)
	tilt_west(grid)
	tilt_south(grid)
	tilt_east(grid)

def calculate_load_on_north_beams(grid):
	total = 0
	for i, line in enumerate(grid):
		total += line.count('O') * (len(grid) - i)
	return total

with open(0) as f:
	grid = [list(line.strip()) for line in f]

for i in range(1, 1000):
	cycle(grid)
	count = calculate_load_on_north_beams(grid)
	print(i, count)
	# analyse results to get answer
