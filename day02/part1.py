file = open("input")

numbers=[]
idgame = 1
max_balls = {
	"red" : 12,
	"green" : 13,
	"blue" : 14,
}
for line in file:
	line = line.split(":")[1]
	games = line.split(";")
	too_many = 0
	for game in games:
		total_balls = {
			"red" : 0,
			"green" : 0,
			"blue" : 0,
		}
		balls = game.split(",")
		for ball in balls:
			number, color = ball.split()
			total_balls[color] += int(number)
		for ball_type in total_balls.keys():
			if total_balls[ball_type] > max_balls[ball_type]:
				too_many = 1
	if not too_many:
		numbers.append(idgame)
	print(idgame, total_balls)
	idgame += 1
print(sum(numbers))

