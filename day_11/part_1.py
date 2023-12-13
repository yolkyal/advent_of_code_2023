with open(0) as f:
	grid = []
	for i, line in enumerate(f):
		grid.append(list(line.strip()))
		if all(c == '.' for c in line.strip()):
			grid.append(list(line.strip()))

expanded_cols = []
for col in range(len(grid[0])):
	if all(grid[row][col] == '.' for row in range(len(grid))):
		expanded_cols.append(col)

for i, col in enumerate(expanded_cols):
	for row in range(len(grid)):
		grid[row].insert(col+i, '.')

galaxies = []
for row in range(len(grid)):
	for col in range(len(grid[0])):
		if grid[row][col] == '#':
			galaxies.append((row, col))

total = 0
for i, galaxy in enumerate(galaxies):
	for j in range(i+1, len(galaxies)):
		other_galaxy = galaxies[j]
		total += abs(other_galaxy[0] - galaxy[0]) + abs(other_galaxy[1] - galaxy[1])

print(total)
