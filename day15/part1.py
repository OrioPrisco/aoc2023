file = open("input")

def hash_alg(string):
	out = 0
	for char in string:
		out += ord(char)
		out *= 17
		out %= 256
	return out

numbers = []
codes = ''.join([line[:-1] for line in file]).split(',')
for code in codes:
	numbers.append(hash_alg(code))
print(sum(numbers))

