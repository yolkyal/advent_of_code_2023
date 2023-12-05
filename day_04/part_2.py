with open(0) as f:
	card_num = 1
	cards = {}
	cards_to_score = []
	for line in f:
		lists = line.strip().partition(': ')[2].split(' | ')
		winning_numbers = lists[0].split()
		numbers_we_have = lists[1].split()
		
		cards[card_num] = (card_num, winning_numbers, numbers_we_have)
		cards_to_score.append((card_num, winning_numbers, numbers_we_have))
		card_num += 1
	
	total = 0
	cards_to_score.reverse()
	while cards_to_score:
		card = cards_to_score.pop()
		score = 0
		for number in card[1]:
			if number in card[2]:
				score += 1
		for i in range(score):
			cards_to_score.append(cards[card[0]+1+i])
		total += 1
	print(total)
