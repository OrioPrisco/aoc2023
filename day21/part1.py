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

for y in range(len(field)):
	for x in range(len(field[0])):
		if field[y][x] == 'S':
			s_pos = (x, y)
			break

def add_neighbour(visitnext, visited, x,y, cost):
	if x < 0 or x >= len(field[0]):
		return
	if y < 0 or y >= len(field):
		return
	node = (x,y)
	cost += 1
	if cost > 64:
		return
	if field[y][x] == '#':
		return
	if node in visited:
		return
	if node in visitnext:
		if visitnext[node] > cost:
			visitnext[node] = cost
	else:
		visitnext[node] = cost

def add_neighbours(visitnext, visited,  node, cost):
	x,y = node
	add_neighbour(visitnext, visited, x + 1, y, cost)
	add_neighbour(visitnext, visited, x - 1, y, cost)
	add_neighbour(visitnext, visited, x, y + 1, cost)
	add_neighbour(visitnext, visited, x, y - 1, cost)


def reachable_tiles(field):
	node = s_pos
	cost = 0
	visitnext = {node : 0}
	visited = {}
	while True:
		if (len(visitnext) == 0):
			return sum([visited[i] % 2 == 0 for i in visited])
		cost = min(visitnext.values())
		nextp = -1
		for i in visitnext:
			if visitnext[i] == cost:
				nextp = i
				break;
		node = nextp
		x,y = node
		visited[node] = visitnext.pop(node)
		add_neighbours(visitnext, visited,  node, cost)

print(reachable_tiles(field))
print(len(field))
print(len(field[0]))
