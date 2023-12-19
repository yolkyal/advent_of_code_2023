from collections import namedtuple

PositionDirection = namedtuple('PositionDirection', 'position direction')

with open(0) as f:
	grid = [list(line.strip()) for line in f]
	
grid_size = len(grid)

visited = set()
attempted = set()
positions_directions_to_check = [PositionDirection((0, -1), (0, 1))]

while positions_directions_to_check:
	pos_dir = positions_directions_to_check.pop()
	if pos_dir in attempted:
		continue
	attempted.add(pos_dir)
	visited.add(pos_dir.position)
	
	next_pos = (pos_dir.position[0] + pos_dir.direction[0], pos_dir.position[1] + pos_dir.direction[1])
	
	if next_pos[0] >= grid_size or next_pos[1] >= grid_size or next_pos[0] < 0 or next_pos[1] < 0:
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

print(len(visited) - 1) # remove off-grid start
