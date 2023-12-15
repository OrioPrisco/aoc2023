file = open("input")

def hash_alg(string):
	out = 0
	for char in string:
		out += ord(char)
		out *= 17
		out %= 256
	return out

def find_lens(box, label):
	for i in range(len(box)):
		if box[i][0] == label:
			return i
	return -1

def del_lens(box, label):
	a = find_lens(box, label)
	if a == -1:
		return
	box.pop(a)

numbers = []
codes = ''.join([line[:-1] for line in file]).split(',')
boxes = [[] for i in range(256)]
for code in codes:
	if '-' in code:
		label = code[:-1]
		del_lens(boxes[hash_alg(label)], label)
	if '=' in code:
		label, value = code.split('=')
		a = find_lens(boxes[hash_alg(label)], label)
		if a == -1:
			boxes[hash_alg(label)].append((label, int(value)))
		else:
			boxes[hash_alg(label)][a] = (label, int(value))
print(boxes)
for i in range(len(boxes)):
	for j in range(len(boxes[i])):
		numbers.append((i+1)*(j+1)*boxes[i][j][1])

print(sum(numbers))

