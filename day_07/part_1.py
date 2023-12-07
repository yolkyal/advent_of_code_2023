from functools import cmp_to_key
from collections import defaultdict

vals = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')

type_map = {
	(5,) : 5,
	(1, 4) : 4,
	(2, 3) : 3,
	(1, 1, 3): 2,
	(1, 2, 2): 1,
	(1, 1, 1, 2): 0
}


def get_type(hand):
	all_counts = defaultdict(int)
	for card in hand:
		all_counts[card] += 1
	counts = tuple(sorted(list(all_counts.values())))
	return type_map.get(counts, -1)


def compare_hands(hand_1, hand_2):
	type_1 = get_type(hand_1)
	type_2 = get_type(hand_2)
	if type_1 != type_2:
		return 1 if type_1 > type_2 else -1
	for i in range(5):
		if hand_1[i] != hand_2[i]:
			return 1 if vals.index(hand_1[i]) < vals.index(hand_2[i]) else -1


with open(0) as f:
	hands_bids = [(line.strip().split()) for line in f]
	
hands_bids.sort(key=cmp_to_key(lambda hand_bid_1, hand_bid_2: compare_hands(hand_bid_1[0], hand_bid_2[0])))

total = 0
for rank, hand_bid in enumerate(hands_bids):
	total += (rank + 1) * int(hand_bid[1])

print(total)
