file = open("input")

field = [line[:-1] for line in file]
empty_verticals   = [all(i == '.' for i in line) for line in field]
empty_horizontals = [all(field[y][x] == '.' for y in range(len(field))) for x in range(len(field[0]))]
galaxies = []

print(empty_verticals)
print(empty_horizontals)

y_offset = 0
for y in range(len(field)):
	if empty_verticals[y]:
		y_offset += 1
		continue
	x_offset = 0
	for x in range(len(field[y])):
		if empty_horizontals[x]:
			x_offset += 1
			continue
		if field[y][x] == '#':
			galaxies.append((x + x_offset, y + y_offset))

print(galaxies)

distances = {}

for galaxy1 in galaxies:
	for galaxy2 in galaxies:
		if galaxy1 == galaxy2:
			continue
		key = (max(galaxy1, galaxy2), min(galaxy1, galaxy2))
		distance = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
		distances[key] = distance
for i in distances:
	print(i, distances[i])
print(sum(distances.values()))

