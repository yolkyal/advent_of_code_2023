vals = {
	'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}

with open(0, 'r') as f:
	total = 0
	for line in f:
		line = line.strip()
		
		first_indexes = [(vals[v], line.find(v)) for v in vals if line.find(v) > -1]
		first = min(first_indexes, key=lambda x: x[1])[0]
		
		last_indexes = [(vals[v], line.rfind(v)) for v in vals if line.find(v) > -1]
		last = max(last_indexes, key=lambda x: x[1])[0]
		
		total += (int(10*first + last))
	print(total)
