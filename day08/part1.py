import re

file = open("input")

moves = file.readline()[:-1]
file.readline()

nodes = {}
for line in file:
	match = re.match("(.{3}) = \((.{3}), (.{3})\)", line)
	id, l, r = match.groups()
	print(id, l, r)
	nodes[id] = {'L' : l, 'R' : r}

steps = 0
curr = 'AAA'
while curr != 'ZZZ':
	curr = nodes[curr][moves[steps % len(moves)]]
	steps += 1

print(steps)

