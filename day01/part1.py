file = open("input")

numbers = []
for line in file:
	first = -1
	last = -1
	for char in line:
		if char.isdigit():
			if first == -1:
				first = int(char)
			last = int(char)
	numbers.append(first * 10 + last)
print(sum(numbers))

