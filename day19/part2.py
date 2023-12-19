import copy

file = open("input")

workflows = {}

def make_workflow(conditions):
	return [condition for condition in conditions.split(',')]

#returns (matching, [others])
def split_part(part, part_prop, comp, value):
	if comp == '=':
		if (value not in part[part_prop]):
			return (None, [part])
		matching = copy.deepcopy(part)
		matching[part_prop] = range(value, value + 1)
		others = []
		other1 = copy.deepcopy(part)
		other2 = copy.deepcopy(part)
		other1[part_prop] = range(value+1, part[part_prop].stop)
		if item_in_range(other1[part_prop]) > 0:
			others.append(other1)
		other2[part_prop] = range(part[part_prop].start, value)
		if item_in_range(other2[part_prop]) > 0:
			others.append(other2)
		return (matching, others)
	if comp == '<':
		if not part[part_prop].start < value:
			return (None, [part])
		matching = copy.deepcopy(part)
		matching[part_prop] = range(part[part_prop].start, min(value, part[part_prop].stop))
		other = copy.deepcopy(part)
		other[part_prop] = range(min(value, part[part_prop].stop), part[part_prop].stop)
		if item_in_range(other[part_prop]) > 0:
			return (matching, [other])
		return (matching, [])
	if comp == '>':
		if not part[part_prop].stop > value:
			return (None, [part])
		matching = copy.deepcopy(part)
		matching[part_prop] = range(max(value + 1, part[part_prop].start) , part[part_prop].stop)
		other = copy.deepcopy(part)
		other[part_prop] = range(part[part_prop].start, max(value + 1, part[part_prop].start))
		if item_in_range(other[part_prop]) > 0:
			return (matching, [other])
		return (matching, [])

def item_in_range(r):
	return r.stop - r.start

def check_workflow(part, workflow_name):
	if part == None:
		return 0
	for propert in part:
		if item_in_range(part[propert]) == 0:
			return 0
	if workflow_name == "R":
		return 0
	if workflow_name == "A":
		total = 1
		for propert in part:
			total *= item_in_range(part[propert])
		return total
	total = 0
	handling = [part]
	to_handle = []
	for condition in workflows[workflow_name]:
		for part in handling:
			if not ':' in condition:
				return total + check_workflow(part, condition)
			cond, dest = condition.split(':')
			propert = cond[0]
			comp = cond[1]
			value = int(cond[2:])
			matching, others = split_part(part, propert, comp, value)
			to_handle += others
			total += check_workflow(matching, dest)
		handling = to_handle
		to_handle = []
	return total


while (line := file.readline().strip()):
	name, conditions = line.split("{")
	workflows[name] = make_workflow(conditions[:-1])

part = {
	'x' : range(1,4001),
	'm' : range(1,4001),
	'a' : range(1,4001),
	's' : range(1,4001),
}
total =  check_workflow(part, "in")

print(total)
