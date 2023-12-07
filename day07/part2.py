file = open("input")

from enum import Enum

class Hand(Enum):
	high_card = 0,
	pair = 1,
	two_pair = 2,
	three = 3,
	house = 4,
	four = 5,
	five = 6,


strength = "J23456789TQKA"

def get_type_nums(nums):
	if nums[5]:
		return Hand.five
	if nums[4]:
		return Hand.four
	if nums[3]:
		if nums[2]:
			return Hand.house
		return Hand.three
	if nums[2] == 2:
		return Hand.two_pair
	if nums[2]:
		return Hand.pair
	return Hand.high_card

def handle_js(js, nums):
	if js == 0:
		return get_type_nums(nums).value[0]
	if js == 5:
		return Hand.five.value[0]
	curr = 0;
	best = 0;
	for i in range(1, len(nums)):
		if nums[i]:
			nums2 = nums.copy()
			nums2[i] -= 1
			nums2[i + 1] += 1
			curr = handle_js(js - 1, nums2)
			print(curr, best)
			best = max(curr, best)
	return best

def get_type(hand):
	seen = {
	"A" : 0,
	"K" : 0,
	"Q" : 0,
	"J" : 0,
	"T" : 0,
	"9" : 0,
	"8" : 0,
	"7" : 0,
	"6" : 0,
	"5" : 0,
	"4" : 0,
	"3" : 0,
	"2" : 0,
	}
	for card in hand:
		seen[card] += 1
	nums = [-1,0,0,0,0,0]
	for card in seen:
		if card == "J":
			continue
		nums[seen[card]] += 1
	js = seen["J"]
	return handle_js(js, nums)
	

numbers = []
hands = []
for line in file:
	hand,bid = line.split()
	hand_type = get_type(hand)
	hand_strength = int("".join([hex(strength.index(i))[2] for i in hand]), 16)
	hands.append((hand_type, hand_strength, hand, int(bid)))

hands.sort()

for i in range(len(hands)):
	print(hands[i][0], hex(hands[i][1]), hands[i][2], hands[i][3], i + 1)
	numbers.append(hands[i][3] * (i + 1))
print(sum(numbers))

