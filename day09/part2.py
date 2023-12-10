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
	print(f"diff = {diff}")
	diff = fix_history(diff)
	print(f"diff = {diff}")
	history = [history[0] - diff[0]] + history
	return history


hists = [fix_history(i) for i in histories ]
print(hists)
print(sum([i[0] for i in hists ]))

