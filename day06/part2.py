import math

file = open("input")

time = int("".join(file.readline().split()[1:]))
distance = int("".join(file.readline().split()[1:]))
numbers = []
ways = 0

def beats(pressed):
	return pressed * (time - pressed) > distance

#finds the first/last value that does not beat the time
def bin_search(upper, lower):
	print(upper, lower)
	if upper == lower:
		return upper
	mid = int((upper + lower) / 2)
	sign = 1 if upper - lower > 0 else -1
	if beats(mid):
		return bin_search(mid - sign, lower)
	return bin_search(upper, mid + sign)

first = bin_search(int(time / 2), 0)
last = bin_search(int(time / 2), time)
print(first,last)
print(last - first)

