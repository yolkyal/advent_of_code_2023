from collections import namedtuple, defaultdict

OFF, ON, LOW, HIGH = False, True, False, True
Pulse = namedtuple('Pulse', 'source destination level')

class Module:
	def __init__(self, name, outputs):
		self.name = name
		self.outputs = outputs

	def __str__(self):
		return f"{self.name} -> {self.outputs}"
	
	def __repr__(self):
		return self.__str__()


class BroadcastModule(Module):
	def __init__(self, name, outputs):
		Module.__init__(self, name, outputs)
	
	def activate(self, pulse):
		return tuple(Pulse(self.name, output, pulse.level) for output in self.outputs)


class FlipFlopModule(Module):
	def __init__(self, name, outputs):
		Module.__init__(self, name, outputs)
		self.state = OFF
	
	def activate(self, pulse):
		if pulse.level == LOW:
			self.state = not self.state
			return tuple(Pulse(self.name, output, self.state) for output in self.outputs)
		else:
			return tuple()


class ConjunctionModule(Module):
	def __init__(self, name, inputs, outputs):
		Module.__init__(self, name, outputs)
		self.last_input_levels = {_input: LOW for _input in inputs}
		
	def activate(self, pulse):
		self.last_input_levels[pulse.source] = pulse.level
		if all(level == HIGH for level in self.last_input_levels.values()):
			return tuple(Pulse(self.name, output, LOW) for output in self.outputs)
		else:
			return tuple(Pulse(self.name, output, HIGH) for output in self.outputs)


def push_button(modules):
	highs = 0
	lows = 0
	
	pulses = [Pulse('button', 'broadcaster', LOW)]
	next_pulses = []
	while pulses:
		for pulse in pulses:
			if pulse.value == HIGH:
				highs += 1
			else:
				lows += 1
			if pulse.destination in modules:
				for output_pulse in modules[pulse.destination].activate(pulse):
					next_pulses.append(output_pulse)
		pulses = next_pulses
		next_pulses = []

	return (highs, lows)


modules = {}
conjunction_modules = {}
input_map = defaultdict(list)
with open(0) as f:
	for line in f:
		module_str, outputs_str = line.strip().split(' -> ')
		outputs = tuple(outputs_str.split(', '))
		if module_str == 'broadcaster':
			modules['broadcaster'] = BroadcastModule('broadcaster', outputs)
		elif module_str[0] == '%':
			modules[module_str[1:]] = FlipFlopModule(module_str[1:], outputs)
		elif module_str[0] == '&':
			conjunction_modules[module_str[1:]] = outputs

		for output in outputs:
			input_map[output].append(module_str[1:] if module_str != 'broadcaster' else 'broadcaster')

for name, outputs in conjunction_modules.items():
	modules[name] = ConjunctionModule(name, {input: 0 for input in input_map[name]}, outputs)

total_highs = 0
total_lows = 0
for i in range(1000):
	highs, lows = push_button(modules)
	total_highs += highs
	total_lows += lows

print(total_highs * total_lows)
