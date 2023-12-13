def count_differences(i, ls1, ls2):
	result = 0
	for i in range(len(ls1)):
		result += sum(1 for a, b in zip(ls1[i], ls2[i]) if a != b)
	return result
		

def get_reflection_index(pattern):
	half_len = len(pattern) // 2
	for i in range(1, half_len + 1):	
		if count_differences(i, pattern[:i], list(reversed(pattern[i:i+i]))) == 1:
			return i
	for i in range(half_len, len(pattern)):
		if count_differences(i, pattern[i-(len(pattern)-i):i], list(reversed(pattern[i:]))) == 1:
			return i


with open(0) as f:
	patterns_r = []
	patterns_c = []
	current_pattern_r = []
	current_pattern_c = []
	for line in f:
		if line.strip():
			current_pattern_r.append(line.strip())
			for i, c in enumerate(line.strip()):
				if i < len(current_pattern_c):
					current_pattern_c[i] += c
				else:
					current_pattern_c.append([c])
		else:
			patterns_r.append(current_pattern_r)
			patterns_c.append(current_pattern_c)
			current_pattern_r = []
			current_pattern_c = []
	patterns_r.append(current_pattern_r)
	patterns_c.append(current_pattern_c)


total = 0
for i in range(len(patterns_r)):
	horizontal_reflection_index = get_reflection_index(patterns_r[i])
	if horizontal_reflection_index:
		total += 100 * horizontal_reflection_index
	
	vertical_reflection_index = get_reflection_index(patterns_c[i])
	if vertical_reflection_index:
		total += vertical_reflection_index

print(total)
