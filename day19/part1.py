file = open("input")

workflows = {}

def make_workflow(conditions):
	return [condition for condition in conditions.split(',')]

def do_comp(part_prop, comp, value):
	if comp == '=':
		return part_prop == value
	if comp == '<':
		return part_prop < value
	if comp == '>':
		return part_prop > value

def check_workflow(part, workflow_name):
	if workflow_name == "R":
		return False
	if workflow_name == "A":
		return True
	for condition in workflows[workflow_name]:
		if not ':' in condition:
			return check_workflow(part, condition)
		cond, dest = condition.split(':')
		propert = cond[0]
		comp = cond[1]
		value = int(cond[2:])
		if do_comp(part[propert], comp, value):
			return check_workflow(part, dest)
	print('uh oh', part, workflow_name, workflows[workflow_name])


while (line := file.readline()).strip():
	name, conditions = line.split("{")
	workflows[name] = make_workflow(conditions[:-2])

total = 0
while (line := file.readline()).strip():
	part = {}
	part_value = 0
	for propert in line[1:-2].split(','):
		key,value = propert.split('=')
		part[key] = int(value)
		part_value += int(value)
	print(part)
	if check_workflow(part, "in"):
		total += part_value

print(total)
