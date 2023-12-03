import re

file = open("input")
lines = str(file.read()).split('\n')
gears = [[[None,None]for i in lines[0]] for i in lines]

def is_gear(lines, i, j):
	if i < 0 or j < 0:
		return False
	if i >= len(lines) or j >= len(lines[i]):
		return False
	c = lines[i][j]
	if c.isdigit() or c == '.':
		return False
	return c == '*'

def add_gear_ratio(i, j, ratio):
	indexes = gears[i][j]
	if indexes == None:
		return
	if indexes[0] == None:
		indexes[0] = ratio
		return
	if indexes[1] != None:
		gears[i][j] = None
		return
	indexes[1] = ratio

def sum_gears():
	total = 0
	for line in gears:
		for gear in line:
			if gear == None:
				continue
			if gear[0] == None or gear[1] == None:
				continue
			total += gear[0] * gear[1]
	return total

def is_part(lines, i, j, span):
	#print(f"{i}; {j}, {span}")
	i -= 1
	j -= 1
	for k in range(span + 2):
		for l in range(3):
			if is_gear(lines, i + l, j + k):
				add_gear_ratio(i + l, j + k, int(lines[i+1][j+1:j+1+span]))

def solve():
	numbers = []
	for i in range(len(lines)):
		j = 0;
		while (res := re.search("\d+", lines[i][j:])):
			print(f"looking at {i};{j} {res.group(0)}")
			is_part(lines, i, res.span()[0] + j, len(res.group(0)))
			j += res.span()[1]
	for i in range(len(gears)):
		for j in range(len(gears[0])):
			if gears[i][j] and gears[i][j][0]:
				print(f"{i} {j} {gears[i][j]}")
	print(sum_gears())

solve()
