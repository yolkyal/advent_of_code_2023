from functools import reduce

with open(0) as f:
	times = [int(t) for t in next(f).strip().replace('Time:', '').split() if t]
	distances = [int(d) for d in next(f).strip().replace('Distance:', '').split() if d]
	
	records = list(zip(times, distances))
	
	num_wins = []
	for time, distance in records:
		wins = 0
		for time_held in range(1, time):
			speed_reached = time_held
			distance_travelled = speed_reached * (time - time_held)
			if distance_travelled > distance:
				wins += 1
		num_wins.append(wins)
		
	result = reduce(lambda x, y: x * y, num_wins)
	
	print(result)
