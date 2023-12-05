from collections import defaultdict, namedtuple

Mapping = namedtuple('Mapping', 'dest_start src_start range_length')

def find_map_val(val, mappings):
	for mapping in mappings:
		if val >= mapping.src_start and val < (mapping.src_start + mapping.range_length):
			return mapping.dest_start + (val - mapping.src_start)
	return val

with open(0) as f:
	seeds = map(int, next(f).strip().replace('seeds: ', '').split())
	
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
	for seed_num in seeds:
		val = seed_num
		for map_set in maps.values():
			val = find_map_val(val, map_set)
		lowest_value = min(lowest_value, val)
	
	print(lowest_value)
