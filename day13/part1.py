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
		if a == b:
			result = i
	for i in range(0, half_len):
		a = pattern[i+i+1:i + half_len+1]
		b = pattern[i+ half_len + 1:]
		b.reverse()
		print(a)
		print(b)
		print(f"=={i+half_len}==")
		if a == b:
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

