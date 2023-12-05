from collections import defaultdict, namedtuple

Mapping = namedtuple('Mapping', 'dest_start src_start range_length')
Wedge = namedtuple('Wedge', 'range_start range_end')


def get_resultant_wedges(wedge, mapping):
	w_start, w_end, m_start, m_end, m_range = wedge.range_start, wedge.range_end, mapping.src_start, mapping.src_start + mapping.range_length, mapping.dest_start - mapping.src_start
	if w_start >= m_start:
		if w_start >= m_end:
			return None
		if w_end > m_end:
			return [Wedge(w_start + m_range, m_end + m_range), Wedge(m_end, w_end)]
		elif w_end <= m_end:
			return [Wedge(w_start + m_range, w_end + m_range)]			
	elif w_start < m_start:
		if w_end <= m_start:
			return None
		if w_end > m_end:
			return [Wedge(m_start + m_range, m_end + m_range), Wedge(w_start, m_start), Wedge(m_end, w_end)]
		elif w_end <= m_end:
			return [Wedge(m_start + m_range, w_end + m_range), Wedge(w_start, m_start)]


def find_wedges(wedges, mappings):
	new_wedges = []
	remaining_wedges = wedges
	
	for wedge in remaining_wedges:
		for mapping in mappings:
			resultant_wedges = get_resultant_wedges(wedge, mapping)
			if resultant_wedges:
				new_wedges.append(resultant_wedges[0])
				remaining_wedges = resultant_wedges[1:]
	return new_wedges + remaining_wedges


with open(0) as f:
	seed_ranges = list(map(int, next(f).strip().replace('seeds: ', '').split()))
	
	seed_num_start_wedges = [Wedge(seed_ranges[i], seed_ranges[i] + seed_ranges[i+1] - 1) for i in range(0, len(seed_ranges) - 1, 2)]
	
	map_no = -1
	maps = defaultdict(list)
	for line in f:
		if not line.strip():
			map_no += 1
		elif not line[0].isdigit():
			continue
		else:
			maps[map_no].append(Mapping(*map(int, line.strip().split())))
	
	lowest_value = 1000000000
	for start_wedge in seed_num_start_wedges:
		wedges = [start_wedge]
		for map_set in maps.values():
			wedges = find_wedges(wedges, map_set)
		for wedge in wedges:
			lowest_value = min(wedge.range_start, lowest_value)
		print(start_wedge, lowest_value)
