def hash(x):
	val = 0
	for c in x:
		val += ord(c)
		val *= 17
		val %= 256
	return val

with open(0) as f:
	steps = next(f).strip().split(',')

total = 0
for step in steps:
	total += hash(step)
print(total)
