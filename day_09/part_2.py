with open(0) as f:
	lines = [list(map(int, line.strip().split())) for line in f]

total = 0
for line in lines:
	extrapolations = [line]	
	while any(val != 0 for val in extrapolations[-1]):
		new_ex = []
		for i in range(len(extrapolations[-1]) - 1):
			new_ex.append(extrapolations[-1][i+1] - extrapolations[-1][i])
		extrapolations.append(new_ex)
		
	for i in range(len(extrapolations) - 2, -1, -1):
		extrapolations[i].insert(0, (extrapolations[i][0] - extrapolations[i+1][0]))
	
	total += extrapolations[0][0]
print(total)
