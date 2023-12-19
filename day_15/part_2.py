from collections import defaultdict

def hash(x):
	val = 0
	for c in x:
		val += ord(c)
		val *= 17
		val %= 256
	return val

def put_lens_into_box(lens, box):
	for i, _lens in enumerate(box):
		if _lens[0] == lens[0]:
			box[i] = lens
			return
	box.append(lens)

def remove_lens_from_box(label, box):
	for i, lens in enumerate(box):
		if lens[0] == label:
			box.pop(i)
			return

steps = []
with open(0) as f:
	steps = next(f).strip().split(',')

boxes = defaultdict(list)
for step in steps:
	if step[-1] == '-':
		label = step[:-1]
		box_number = hash(label)
		remove_lens_from_box(label, boxes[box_number])	
	else:
		label, focal_length = step.split('=')
		box_number = hash(label)
		put_lens_into_box((label, focal_length), boxes[box_number])

total = 0
for box_number, box in boxes.items():
	for slot_number, lens in enumerate(box):
		total += (1 + box_number) * (1 + slot_number) * int(lens[1])
print(total)
