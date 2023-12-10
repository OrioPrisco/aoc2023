file = open("input")

field = [line for line in file]
costs = [[0 for i in field[0]] for i in field]

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
}

rev_dir = {
	"N" : "S",
	"S" : "N",
	"E" : "W",
	"W" : "E",
}

def add_coord(a,b):
	return (a[0] + b[0], a[1] + b[1])

for direction in dir_to_coord:
	x,y = add_coord(s_pos, dir_to_coord[direction])
	if rev_dir[direction] in char_to_dir[field[y][x]]:
		char_to_dir["S"] += direction

def bfs(x, y):
	visitnext = [((x, y), 1)]
	cost = 0
	while 1:
		if (len(visitnext) == 0):
			return cost - 2
		coord, cost = visitnext.pop(0)
		x,y = coord
		print(f"looking at {x},{y} ({cost})")
		if (costs[y][x] <= cost and costs[y][x] != 0):
			continue
		costs[y][x] = cost
		for direction in char_to_dir[field[y][x]]:
			visitnext.append((add_coord(dir_to_coord[direction], (x,y)), cost + 1))

answer = bfs(s_pos[0], s_pos[1])
for i in costs:
	print(i)
print(answer)

