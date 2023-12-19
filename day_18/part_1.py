from collections import namedtuple

DigInstruction = namedtuple('DigInstruction', 'direction distance color')

dig_instructions = []
with open(0) as f:
	for line in f:
		direction, distance, color = line.strip().split()
		dig_instructions.append(DigInstruction(direction, int(distance), color))

dig_loop = set()
current_position = (0, 0)
for dig_instruction in dig_instructions:
	if dig_instruction.direction == 'U':
		for i in range(dig_instruction.distance):
			current_position = (current_position[0], current_position[1] - 1)
			dig_loop.add(current_position)
	elif dig_instruction.direction == 'D':
		for i in range(dig_instruction.distance):
			current_position = (current_position[0], current_position[1] + 1)
			dig_loop.add(current_position)
	elif dig_instruction.direction == 'L':
		for i in range(dig_instruction.distance):
			current_position = (current_position[0] - 1, current_position[1])
			dig_loop.add(current_position)
	elif dig_instruction.direction == 'R':
		for i in range(dig_instruction.distance):
			current_position = (current_position[0] + 1, current_position[1])
			dig_loop.add(current_position)

in_bounds = dig_loop
left_to_check = [(1, 1)]
while left_to_check:
	pos = left_to_check.pop()
	if pos not in in_bounds:
		in_bounds.add(pos)
		left_to_check += [(pos[0]-1, pos[1]), (pos[0]+1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1)]
print(len(in_bounds))
