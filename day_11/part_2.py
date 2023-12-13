EXPANSION_SIZE = 999999

expanded_rows = []
with open(0) as f:
	grid = []
	for i, line in enumerate(f):
		grid.append(list(line.strip()))
		if all(c == '.' for c in line.strip()):
			expanded_rows.append(i)

expanded_cols = []
for col in range(len(grid[0])):
	if all(grid[row][col] == '.' for row in range(len(grid))):
		expanded_cols.append(col)

galaxies = []
for row in range(len(grid)):
	for col in range(len(grid[0])):
		if grid[row][col] == '#':
			expanded_row_count = len([e_row for e_row in expanded_rows if e_row < row])
			expanded_col_count = len([e_col for e_col in expanded_cols if e_col < col])
			galaxies.append((row + EXPANSION_SIZE * expanded_row_count, col + EXPANSION_SIZE * expanded_col_count))

total = 0
for i, galaxy in enumerate(galaxies):
	for j in range(i+1, len(galaxies)):
		other_galaxy = galaxies[j]
		total += abs(other_galaxy[0] - galaxy[0]) + abs(other_galaxy[1] - galaxy[1])

print(total)
