from functools import reduce

start_nodes = []
with open(0) as f:
	directions = next(f).strip()
	next(f)
	
	nodes = {}
	for line in f:
		key, val = line.strip().split(' = ')
		nodes[key] = tuple(val.replace('(', '').replace(')', '').split(', '))
		if key[2] == 'A':
			start_nodes.append(key)

path_lengths = []
for node in start_nodes:
	path = []
	while not node in path:
		path.append(node)
		for direction in directions:
			if direction == 'L':
				node = nodes[node][0]
			elif direction == 'R':
				node = nodes[node][1]
	length_of_path = len(path) - path.index(node)
	path_lengths.append(length_of_path)

result = reduce(lambda x, y: x * y, path_lengths) * len(directions)
print(result)
