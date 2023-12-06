import math

file = open("input")

times = [int(i) for i in file.readline().split()[1:]]
distances = [int(i) for i in file.readline().split()[1:]]
numbers = []
for i in range(len(times)):
	time = times[i]
	distance = distances[i]
	ways = 0
	for pressed in range(time):
		if pressed * (time - pressed) > distance:
			ways += 1
	numbers.append(ways)

print(math.prod(numbers))

