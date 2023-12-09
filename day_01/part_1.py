def get_first_digit(s):
	for c in s:
		if c.isdigit():
			return c
	
def get_last_digit(s):
	for c in s[::-1]:
		if c.isdigit():
			return c

with open(0, 'r') as f:
	total = 0
	for line in f:
		first = get_first_digit(line)
		last = get_last_digit(line)
		total += int(first + last)
	print(total)
