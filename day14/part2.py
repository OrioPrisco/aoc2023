file = open("input")

from functools import cache

field = [line[:-1] for line in file]
numbers = []
def roll(field, xdiff, ydiff):
	keep_going = True
	while keep_going:
		keep_going = False
		for y in range(1 if ydiff == -1 else 0, len(field) - (1 if ydiff == 1 else 0)):
			for x in range(1 if xdiff == -1 else 0, len(field[0]) - (1 if xdiff == 1 else 0)):
				if field[y][x] == '.' and field[y + ydiff][x + xdiff] == 'O':
					field[y][x] = 'O'
					field[y+ ydiff][x + xdiff] = '.'
					keep_going = True

@cache
def roll_str(strs, xdiff, ydiff):
	tab = [[c for c in line] for line in strs]
	roll(tab, xdiff, ydiff)
	lines = tuple([''.join(line) for line in tab])
	return lines

dirs = [
	(0,1),
	(1,0),
	(0,-1),
	(-1,0)
]
#pattern -> when
seen = {}

lines = tuple([''.join(line) for line in field])
i = 0
todo = 1000000000
while i < todo:
	key = hash(lines)
	if (lines in seen):
		print(f"loop at {i} {seen[lines]}")
		loop_len = i - seen[lines]
		cycles_left = todo - i
		skippable_loops = int(cycles_left / loop_len)
		print(f"skipping {skippable_loops * loop_len}")
		i += skippable_loops * loop_len
	else:
		seen[lines] = i
	for x,y in dirs:
		lines = roll_str(lines, x, y)
	if i % 1000 == 0:
		print(f"{100*i/1000000000}%")
	i += 1
field = [[c for c in line] for line in lines]

for line,value in zip(field, range(len(field), 0, -1)):
	for char in line:
		if char == 'O':
			numbers.append(value)
print(sum(numbers))

