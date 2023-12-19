from collections import namedtuple

Rule = namedtuple('Rule', 'category gtlt val destination') 
Workflow = namedtuple('Workflow', 'rules default')
Part = namedtuple('Part', 'x, m, a, s')

workflows = {}
parts = []
with open(0) as f:
	for line in f:
		if line[0] != '{':
			name, _, rule_text = line.strip().partition('{')
			rule_strs = rule_text[:-1].split(',')
			rules = []
			default = rule_strs[-1]
			for rule_str in rule_strs[:-1]:
				rule_str, _, destination = rule_str.rpartition(':')
				if '>' in rule_str:
					category, gtlt, val = rule_str.partition('>')
				elif '<' in rule_str:
					category, gtlt, val = rule_str.partition('<')
				rules.append(Rule(category, gtlt, int(val), destination))	
			workflows[name] = Workflow(rules, default)
		elif line[0] == '{':
			x, m, a, s = map(lambda p:int(p.partition('=')[2]), line.strip().replace('{', '').replace('}', '').split(','))
			parts.append(Part(x, m, a, s))

total = 0
for part in parts:
	cur = 'in'
	while cur not in ('A', 'R'):
		workflow = workflows[cur]
		for rule in workflow.rules:
			if rule.gtlt == '>':
				if rule.category == 'x' and part.x > rule.val:
					cur = rule.destination
				elif rule.category == 'm' and part.m > rule.val:
					cur = rule.destination
				elif rule.category == 'a' and part.a > rule.val:
					cur = rule.destination
				elif rule.category == 's' and part.s > rule.val:
					cur = rule.destination
			elif rule.gtlt == '<':
				if rule.category == 'x' and part.x < rule.val:
					cur = rule.destination
				elif rule.category == 'm' and part.m < rule.val:
					cur = rule.destination
				elif rule.category == 'a' and part.a < rule.val:
					cur = rule.destination
				elif rule.category == 's' and part.s < rule.val:
					cur = rule.destination
			if cur in ('A', 'R') or workflow != workflows[cur]:
				break
		if cur in workflows and workflow == workflows[cur]:
			cur = workflow.default
	if cur == 'A':
		total += part.x + part.m + part.a + part.s
print(total)
