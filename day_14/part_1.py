with open(0) as f:
	grid = [list(line.strip()) for line in f]

for line_num in range(len(grid)):
	if line_num == 0:
		continue
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

total = 0
for i, line in enumerate(grid):
	total += line.count('O') * (len(grid) - i)
print(total)
