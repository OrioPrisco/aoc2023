file = open("input")

field = [[c for c in line[:-1]] for line in file]
numbers = []
keep_going = True
while keep_going:
	keep_going = False
	for y in range(0, len(field) - 1):
		for x in range(len(field[0])):
			if field[y][x] == '.' and field[y + 1][x] == 'O':
				field[y][x] = 'O'
				field[y+1][x] = '.'
				keep_going = True

for l in field:
	for c in l:
		print(c, end="")
	print()

for line,value in zip(field, range(len(field), 0, -1)):
	for char in line:
		if char == 'O':
			numbers.append(value)
print(sum(numbers))

