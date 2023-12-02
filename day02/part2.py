file = open("input")

numbers=[]
for line in file:
	total_cubes = {
		"red" : 0,
		"green" : 0,
		"blue" : 0,
	}
	line = line.split(":")[1]
	games = line.split(";")
	for game in games:
		cubes = game.split(",")
		for cube in cubes:
			number, color = cube.split()
			total_cubes[color] = max(int(number), total_cubes[color])
	power = 1
	for key in total_cubes:
		power *= total_cubes[key]
	numbers.append(power)
print(sum(numbers))

