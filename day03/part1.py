import re

file = open("input")
lines = str(file.read()).split('\n')

def is_symbol(lines, i, j):
	if i < 0 or j < 0:
		return False
	if i >= len(lines) or j >= len(lines[i]):
		return False
	c = lines[i][j]
	if c.isdigit() or c == '.':
		return False
	return True

def is_part(lines, i, j, span):
	print(f"{i}; {j}, {span}")
	i -= 1
	j -= 1
	for k in range(span + 2):
		for l in range(3):
			if is_symbol(lines, i + l, j + k):
				print(f"Found {lines[i+l][j+k]} at {i+l};{j+k}")
				return True
	return False

def solve():
	numbers = []
	numss = []
	for i in range(len(lines)):
		j = 0;
		nums = []
		while (res := re.search("\d+", lines[i][j:])):
			print(f"looking at {i};{j} {res.group(0)}")
			if is_part(lines, i, res.span()[0] + j, len(res.group(0))):
				numbers.append(int(res.group(0)))
				nums.append(int(res.group(0)))
			j += res.span()[1]
		numss.append(nums)
	for i in numss:
		print(i)
	print(numbers)
	print(sum(numbers))
solve()
