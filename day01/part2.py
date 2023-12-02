file = open("input")

spelled_out = {
	"one" : 1,
	"two" : 2,
	"three" : 3,
	"four" : 4,
	"five" : 5,
	"six" : 6,
	"seven" : 7,
	"eight" : 8,
	"nine" : 9,
	"1" : 1,
	"2" : 2,
	"3" : 3,
	"4" : 4,
	"5" : 5,
	"6" : 6,
	"7" : 7,
	"8" : 8,
	"9" : 9,
	"0" : 0,
}

numbers = []
for line in file:
	first = -1
	last = -1
	for i in range(len(line)):
		for key in spelled_out.keys():
			if line[i:].startswith(key):
				if first == -1:
					first = spelled_out[key]
				last = spelled_out[key]
	numbers.append(first * 10 + last)
print(sum(numbers))

