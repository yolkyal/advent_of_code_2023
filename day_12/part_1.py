from more_itertools import powerset


def hash_counts(pattern):
	counts = []
	last_c = None
	for c in pattern:
		if c == '#':
			if last_c == '#':
				counts[-1] += 1
			else:
				counts.append(1)
		last_c = c
	return counts


def replace_question_marks(pattern, hash_replace_indexes):
	new_pattern = []
	for i, c in enumerate(pattern):
		if i in hash_replace_indexes:
			new_pattern.append('#')
		elif c == '?':
			new_pattern.append('.')
		else:
			new_pattern.append(c)
	return new_pattern


def get_permutations(pattern):
	unknown_indexes = []
	for i, c in enumerate(pattern):
		if c == '?':
			unknown_indexes.append(i)
	
	return [replace_question_marks(pattern, indexes) for indexes in powerset(unknown_indexes)]
		

with open(0) as f:
	patterns_counts = []
	for line in f:
		pattern, counts = line.strip().split()
		patterns_counts.append((list(pattern), list(map(int, counts.split(',')))))

total = 0
for pattern, counts in patterns_counts:
	perm_count = 0
	for permutation in get_permutations(pattern):
		if hash_counts(permutation) == counts:
			perm_count += 1
	total += perm_count
print(total)
