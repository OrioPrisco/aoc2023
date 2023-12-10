file = open("input")

field = [line for line in file]
pipes = [[' ' for i in field[0]] for i in field]
tags  = [[' ' for i in field[0]] for i in field]

s_pos = None

for y in range(len(field)):
	for x in range(len(field[0])):
		if field[y][x] == 'S':
			s_pos = (x, y)
			break

char_to_dir = {
	"." : "",
	"|" : "NS",
	"-" : "EW",
	"F" : "SE",
	"J" : "NW",
	"7" : "SW",
	"L" : "NE",
	"S" : ""
}

dir_to_coord = {
	"N" : ( 0, -1),
	"S" : ( 0,  1),
	"E" : ( 1,  0),
	"W" : (-1,  0),
	""  : ( 0,  0),
}

rev_dir = {
	"N" : "S",
	"S" : "N",
	"E" : "W",
	"W" : "E",
	""  : "",
}

def add_coord(a,b):
	return (a[0] + b[0], a[1] + b[1])

def tag_direction(tag, x, y, direction):
	x,y = add_coord((x,y), dir_to_coord[direction])
	tags[y][x] = tag

def tag_surrounding(char, x, y, dire):
	#tag_direction(dire, x,y, "")
	#return
	if char == "|":
		tag_direction("l" if dire == "N" else "r", x ,y, "W")
		tag_direction("r" if dire == "N" else "l", x ,y, "E")
	if char == "-":
		tag_direction("l" if dire == "E" else "r", x ,y, "N")
		tag_direction("r" if dire == "E" else "l", x ,y, "S")
	if char == "F":
		tag_direction("l" if dire == "N" else "r", x ,y, "N")
		tag_direction("l" if dire == "N" else "r", x ,y, "W")
	if char == "J":
		tag_direction("l" if dire == "S" else "r", x ,y, "S")
		tag_direction("l" if dire == "S" else "r", x ,y, "E")
	if char == "7":
		tag_direction("l" if dire == "E" else "r", x ,y, "N")
		tag_direction("l" if dire == "E" else "r", x ,y, "E")
	if char == "L":
		tag_direction("l" if dire == "W" else "r", x ,y, "S")
		tag_direction("l" if dire == "W" else "r", x ,y, "W")
	if char == "S":
		return
		#doesn't matter in my input


for direction in dir_to_coord:
	x,y = add_coord(s_pos, dir_to_coord[direction])
	if rev_dir[direction] in char_to_dir[field[y][x]]:
		char_to_dir["S"] += direction
		break

def bfs(x, y):
	visitnext = [((x, y), None)]
	while 1:
		if len(visitnext) == 0:
			return
		coord, dire  = visitnext.pop(0)
		x,y = coord
		if (pipes[y][x] != ' '):
			continue
		tag_surrounding(field[y][x], x, y, dire)
		pipes[y][x] = field[y][x]
		for direction in char_to_dir[field[y][x]]:
			visitnext.append( (add_coord(dir_to_coord[direction], (x,y)), direction) )

def print_tab(tab):
	for i in tab:
		for j in i:
			print(j, end="")
		print()
bfs(s_pos[0], s_pos[1])
print_tab(pipes)
print_tab(tags)

fused = [[' ' for i in field[0]] for i in field]
for y in range(len(fused)):
	for x in range(len(fused[0])):
		if pipes[y][x] != ' ':
			fused[y][x] = pipes[y][x]
		else:
			fused[y][x] = tags[y][x]

def flood_fill(x,y,char, override = 1):
	if x < 0 or x > len(fused[0]):
		return
	if y < 0 or y > len(fused):
		return
	if fused[y][x] != ' ' and not override:
		return
	fused[y][x] = char
	flood_fill(x + 1, y    , char, 0)
	flood_fill(x - 1, y    , char, 0)
	flood_fill(x    , y + 1, char, 0)
	flood_fill(x    , y - 1, char, 0)

for y in range(len(fused)):
	for x in range(len(fused[0])):
		if fused[y][x] == 'r':
			flood_fill(x,y, fused[y][x])
print_tab(fused)

total = 0
for y in range(len(fused)):
	for x in range(len(fused[0])):
		if fused[y][x] == 'r':
			total += 1
print(total)
