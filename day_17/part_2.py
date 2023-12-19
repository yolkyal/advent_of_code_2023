from collections import namedtuple

Endpoint = namedtuple('Endpoint', 'pos last_direction steps_in_direction')

def get_next(endpoint, grid):
	if endpoint.steps_in_direction < 4:
		return [Endpoint((endpoint.pos[0] + endpoint.last_direction[0], endpoint.pos[1] + endpoint.last_direction[1]), endpoint.last_direction, endpoint.steps_in_direction + 1)]

	ls_new_endpoint_pos = [(endpoint.pos[0]+1, endpoint.pos[1]), (endpoint.pos[0], endpoint.pos[1]+1), (endpoint.pos[0]-1, endpoint.pos[1]), (endpoint.pos[0], endpoint.pos[1]-1)]
	if endpoint.steps_in_direction == 10:
		if endpoint.last_direction == (1, 0):
			ls_new_endpoint_pos.remove((endpoint.pos[0]+1, endpoint.pos[1]))
		elif endpoint.last_direction == (0, 1):
			ls_new_endpoint_pos.remove((endpoint.pos[0], endpoint.pos[1]+1))
		elif endpoint.last_direction == (-1, 0):
			ls_new_endpoint_pos.remove((endpoint.pos[0]-1, endpoint.pos[1]))
		elif endpoint.last_direction == (0, -1):
			ls_new_endpoint_pos.remove((endpoint.pos[0], endpoint.pos[1]-1))
	
	if endpoint.last_direction == (1, 0):
		ls_new_endpoint_pos.remove((endpoint.pos[0]-1, endpoint.pos[1]))
	elif endpoint.last_direction == (0, 1):
		ls_new_endpoint_pos.remove((endpoint.pos[0], endpoint.pos[1]-1))
	elif endpoint.last_direction == (-1, 0):
		ls_new_endpoint_pos.remove((endpoint.pos[0]+1, endpoint.pos[1]))
	elif endpoint.last_direction == (0, -1):
		ls_new_endpoint_pos.remove((endpoint.pos[0], endpoint.pos[1]+1))
	
	new_endpoints = []
	for new_endpoint_pos in ls_new_endpoint_pos:
		direction = (new_endpoint_pos[0] - endpoint.pos[0], new_endpoint_pos[1] - endpoint.pos[1])
		if direction == endpoint.last_direction:
			new_endpoints.append(Endpoint(new_endpoint_pos, direction, endpoint.steps_in_direction + 1))
		else:
			new_endpoints.append(Endpoint(new_endpoint_pos, direction, 1))
	
	return new_endpoints

def dijkstra(grid, source, target):
	dist = {}
	dist[Endpoint(source, (0, 1), 0)] = 0

	endpoints = {Endpoint(source, (0, 1), 0)}
	while len(endpoints) > 0:
		endpoint = min(endpoints, key=lambda e: dist[e])
		
		endpoints.remove(endpoint)
		if endpoint.pos == target:
			if endpoint.steps_in_direction >= 4:
				return dist[endpoint]
			else:
				continue
		
		new_endpoints = get_next(endpoint, grid)
		for new_endpoint in new_endpoints:
			if new_endpoint.pos in grid:
				alt = dist[endpoint] + grid[new_endpoint.pos]
				if alt < dist.get(new_endpoint, 10000000):
					endpoints.add(new_endpoint)
					dist[new_endpoint] = alt

grid = {}
with open(0) as f:
	for row, line in enumerate(f):
		grid_size = len(line.strip())
		for col, val in enumerate(line.strip()):
			grid[(row, col)] = int(val)

target = (grid_size - 1, grid_size - 1)

result = dijkstra(grid, (0, 0), target)
print(result)
