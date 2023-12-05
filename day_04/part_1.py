with open(0) as f:
	total = 0
	for line in f:
		lists = line.strip().partition(': ')[2].split(' | ')
		winning_numbers = lists[0].split()
		numbers_we_have = lists[1].split()
		score = 0
		for number in winning_numbers:
			if number in numbers_we_have:
				score = score * 2 if score > 0 else 1
		total += score
	print(total)
