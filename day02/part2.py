file = open("input")

numbers=[]
for line in file:
	total_balls = {
		"red" : 0,
		"green" : 0,
		"blue" : 0,
	}
	line = line.split(":")[1]
	games = line.split(";")
	for game in games:
		balls = game.split(",")
		for ball in balls:
			number, color = ball.split()
			total_balls[color] = max(int(number), total_balls[color])
	power = 1
	for key in total_balls:
		power *= total_balls[key]
	numbers.append(power)
print(sum(numbers))

