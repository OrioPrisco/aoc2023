file = open("input")

numbers = []
for line in file:
	winning = []
	matching = -1
	line = line.split(":")[1]
	for number in line.split("|")[0].split():
		winning.append(number)
	for number in line.split("|")[1].split():
		if number in winning:
			matching += 1
	if matching > -1:
		numbers.append(2 ** matching)
print(sum(numbers))
