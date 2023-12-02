file = open("input")

numbers=[]
idgame = 1
max_cubes = {
	"red" : 12,
	"green" : 13,
	"blue" : 14,
}
for line in file:
	line = line.split(":")[1]
	games = line.split(";")
	too_many = 0
	for game in games:
		total_cubes = {
			"red" : 0,
			"green" : 0,
			"blue" : 0,
		}
		cubes = game.split(",")
		for cube in cubes:
			number, color = cube.split()
			total_cubes[color] += int(number)
		for cube_type in total_cubes.keys():
			if total_cubes[cube_type] > max_cubes[cube_type]:
				too_many = 1
	if not too_many:
		numbers.append(idgame)
	print(idgame, total_cubes)
	idgame += 1
print(sum(numbers))

