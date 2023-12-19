from collections import namedtuple

PositionDirection = namedtuple('PositionDirection', 'position direction')

def count_energised(grid, start_pos_dir):
	visited = set()
	attempted = set()
	positions_directions_to_check = [start_pos_dir]
	
	while positions_directions_to_check:
		pos_dir = positions_directions_to_check.pop()
		if pos_dir in attempted:
			continue
		attempted.add(pos_dir)
		visited.add(pos_dir.position)
		
		next_pos = (pos_dir.position[0] + pos_dir.direction[0], pos_dir.position[1] + pos_dir.direction[1])
		
		if next_pos[0] >= len(grid) or next_pos[1] >= len(grid) or next_pos[0] < 0 or next_pos[1] < 0:
			continue
		if grid[next_pos[0]][next_pos[1]] == '.':
			positions_directions_to_check.append(PositionDirection(next_pos, pos_dir.direction))
		elif grid[next_pos[0]][next_pos[1]] == '\\':
			if pos_dir.direction == (0, 1):
				positions_directions_to_check.append(PositionDirection(next_pos, (1, 0)))
			elif pos_dir.direction == (1, 0):
				positions_directions_to_check.append(PositionDirection(next_pos, (0, 1)))
			elif pos_dir.direction == (-1, 0):
				positions_directions_to_check.append(PositionDirection(next_pos, (0, -1)))
			elif pos_dir.direction == (0, -1):
				positions_directions_to_check.append(PositionDirection(next_pos, (-1, 0)))
		elif grid[next_pos[0]][next_pos[1]] == '/':
			if pos_dir.direction == (0, 1):
				positions_directions_to_check.append(PositionDirection(next_pos, (-1, 0)))
			elif pos_dir.direction == (1, 0):
				positions_directions_to_check.append(PositionDirection(next_pos, (0, -1)))
			elif pos_dir.direction == (-1, 0):
				positions_directions_to_check.append(PositionDirection(next_pos, (0, 1)))
			elif pos_dir.direction == (0, -1):
				positions_directions_to_check.append(PositionDirection(next_pos, (1, 0)))
		elif grid[next_pos[0]][next_pos[1]] == '-':
			if pos_dir.direction in ((0, 1), (0, -1)):
				positions_directions_to_check.append(PositionDirection(next_pos, pos_dir.direction))
			else:
				positions_directions_to_check.append(PositionDirection(next_pos, (0, 1)))
				positions_directions_to_check.append(PositionDirection(next_pos, (0, -1)))
		elif grid[next_pos[0]][next_pos[1]] == '|':
			if pos_dir.direction in ((1, 0), (-1, 0)):
				positions_directions_to_check.append(PositionDirection(next_pos, pos_dir.direction))
			else:
				positions_directions_to_check.append(PositionDirection(next_pos, (1, 0)))
				positions_directions_to_check.append(PositionDirection(next_pos, (-1, 0)))

	return (len(visited) - 1) # remove off-grid start

with open(0) as f:
	grid = [list(line.strip()) for line in f]

best = 0
for i in range(len(grid)):
	print(f'Checked {i} of {len(grid)}...')
	best = max(best, count_energised(grid, PositionDirection((i, -1), (0, 1))))
	best = max(best, count_energised(grid, PositionDirection((i, len(grid)), (0, -1))))
	best = max(best, count_energised(grid, PositionDirection((-1, i), (1, 0))))
	best = max(best, count_energised(grid, PositionDirection((len(grid), i), (-1, 0))))
	
print(best)
