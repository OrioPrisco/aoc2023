file = open("input")

patterns = []
pattern = []
for line in file:
	if line == "\n":
		patterns.append(pattern)
		pattern = []
	else:
		pattern.append(line[:-1])
patterns.append(pattern)

def difference_str(s1, s2):
	return sum([0 if a == b else 1 for a,b in zip(s1, s2)])

def difference_lst(l1, l2):
	return sum([difference_str(a,b) for a,b in zip(l1, l2)])

def get_mirror(pattern):
	result = 0
	half_len = int(len(pattern)/2)
	for i in range(0, 1+half_len):
		a = pattern[:i]
		b = pattern[i:i+i]
		b.reverse()
		print(a)
		print(b)
		print(f"=={i}==")
		if difference_lst(a,b) == 1:
			result = i
	for i in range(0, half_len):
		a = pattern[i+i+1:i + half_len+1]
		b = pattern[i+ half_len + 1:]
		b.reverse()
		print(a)
		print(b)
		print(f"=={i+half_len}==")
		if difference_lst(a,b) == 1:
			result = half_len + i + 1
	return result

def solve(pattern):
	for i in range(len(pattern)):
		print(i, pattern[i])
	rows = get_mirror(pattern)
	print(rows, "rows")
	foo = [''.join(x) for x in zip(*reversed(pattern))]
	for i in range(len(foo)):
		print(i, foo[i])
	cols = get_mirror(foo)
	print(cols, "cols")
	return rows * 100 + cols

numbers = []
for pattern in patterns:
	number = solve(pattern)
	print(number)
	numbers.append(number)

print(sum(numbers))

