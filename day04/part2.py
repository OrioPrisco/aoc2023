file = open("input")

cards = [1 for i in range(198)]
id = 0
for line in file:
	winning = []
	matching = 0
	line = line.split(":")[1]
	for number in line.split("|")[0].split():
		winning.append(number)
	for number in line.split("|")[1].split():
		if number in winning:
			matching += 1
	for i in range(matching):
		cards[id + 1 + i] += cards[id]
	id += 1
print(sum(cards))
