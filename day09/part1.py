file = open("input")

histories = []
for line in file:
	histories.append([int(i) for i in line.split()])

def generate_diff(history):
	out = []
	for i in range(1, len(history)):
		out.append(history[i] - history[i - 1])
	return out

def fix_history(history):
	if all([ v == 0 for v in history ]):
		return history + [0]
	diff = generate_diff(history)
	fix_history(diff)
	history += [history[-1] + diff[-1]]
	return history

print(sum([fix_history(i)[-1] for i in histories ]))

