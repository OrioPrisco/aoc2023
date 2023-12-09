import re

file = open("input")

moves = file.readline()[:-1]
file.readline()

nodes = {}
for line in file:
	match = re.match("(.{3}) = \((.{3}), (.{3})\)", line)
	id, l, r = match.groups()
	nodes[id] = {'L' : l, 'R' : r}

currs = []

for key in nodes:
	if key[2] == 'A':
		currs.append(key)

def solve1(curr):
	steps = 0
	while curr[2] != 'Z':
		curr = nodes[curr][moves[steps % len(moves)]]
		steps += 1
	return steps

import math

sols = [solve1(i) for i in currs]
print(sols)
out = 1
for sol in sols:
	out = math.lcm(out, sol)
print(out)

