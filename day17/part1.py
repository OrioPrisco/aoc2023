file = open("input")
field = [line[:-1] for line in file]

Up    = 0
Left  = 1
Down  = 2
Right = 3

int_to_dir = {
	Up    : ( 0,-1),
	Left  : (-1, 0),
	Down  : ( 0, 1),
	Right : ( 1, 0),
}

def add_neighbour(visitnext, visited, x,y,dire,length, cost):
	addx, addy = int_to_dir[dire]
	x += addx
	y += addy
	if x < 0 or x >= len(field[0]):
		return
	if y < 0 or y >= len(field):
		return
	node = (x,y,dire,length)
	cost += int(field[y][x])
	if node in visited:
		return
	if node in visitnext:
		if visitnext[node] > cost:
			visitnext[node] = cost
	else:
		visitnext[node] = cost

def add_neighbours(visitnext, visited,  node, cost):
	x,y,dire,length = node
	if length < 2:
		add_neighbour(visitnext, visited, x, y, dire, length + 1, cost)
	add_neighbour(visitnext, visited, x, y, (dire + 1) % 4, 0, cost)
	add_neighbour(visitnext, visited, x, y, (dire + 3) % 4, 0, cost)


def distance_to_bottom_left(field):
	node = (0,0,Right,0)
	cost = 0
	visitnext = {node : 0}
	visited = {}
	while True:
		if (len(visitnext) == 0):
			return -1
		cost = min(visitnext.values())
		nextp = -1
		for i in visitnext:
			if visitnext[i] == cost:
				nextp = i
				break;
		node = nextp
		x,y,dire,length = node
		if (x == len(field[0]) - 1) and (y == len(field) - 1):
			print(visited, visitnext)
			return cost
		visited[node] = visitnext.pop(node)
		add_neighbours(visitnext, visited,  node, cost)

print(distance_to_bottom_left(field))
