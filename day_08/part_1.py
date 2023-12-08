with open(0) as f:
	directions = next(f).strip()
	next(f)
	
	nodes = {}
	for line in f:
		key, val = line.strip().split(' = ')
		nodes[key] = tuple(val.replace('(', '').replace(')', '').split(', '))

steps = 0
node = 'AAA'
while node != 'ZZZ':
	for direction in directions:
		if direction == 'L':
			node = nodes[node][0]
		elif direction == 'R':
			node = nodes[node][1]
		steps += 1

print(steps)
