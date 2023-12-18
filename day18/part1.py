file = open("input")

field = [[' ' for i in range(1000)] for j in range(1000)]

s_pos = (500, 500)


dir_to_coord = {
	"U" : ( 0, -1),
	"D" : ( 0,  1),
	"R" : ( 1,  0),
	"L" : (-1,  0),
}

def add_coord(a,b):
	return (a[0] + b[0], a[1] + b[1])

instructions = [line.split() for line in file]

for instruction in instructions:
	direction, number, color = instruction
	for _ in range(int(number)):
		s_pos = add_coord(s_pos, dir_to_coord[direction])
		x,y = s_pos
		field[y][x] = '#'

field2 = []

for i in field:
	if '#' in i:
		field2.append(i)
field = [list(i) for i in zip(*field2)]
field2 = []
for i in field:
	if '#' in i:
		field2.append(i)

def print_tab(f):
	for i in f:
		for j in i:
			print(j, end="")
		print()

print_tab(field2)

def flood_fill(x,y, field):
	todo = [(x,y)]
	while len(todo):
		x,y = todo.pop(0)
		if x < 0 or x > len(field[0]):
			continue
		if y < 0 or y > len(field):
			continue
		if field[y][x] != ' ':
			continue
		field[y][x] = '#'
		todo.append((x + 1, y    ))
		todo.append((x - 1, y    ))
		todo.append((x    , y + 1))
		todo.append((x    , y - 1))

for x in range(len(field2[0])):
	if field2[0][x] == '#':
		print(x+1,1)
		flood_fill(x+1,1,field2)
		break

print_tab(field2)
print(sum([sum([j != ' ' for j in i]) for i in field]))
