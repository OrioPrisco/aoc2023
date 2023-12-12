file = open("input")

from functools import cache
from enum import Enum

class Mode(Enum):
	skip_dot = 0
	match_hash = 1
	next_rule = 2

@cache
def solve(mode, springs, rules):
	if mode == Mode.next_rule:
		rules = rules[1:]
		if len(springs) == 0:
			return 1 if len(rules) == 0 else 0
		if springs[0] == '#':
			return 0
		return solve(Mode.skip_dot, springs[1:], rules)
	
	if mode == Mode.skip_dot:
		if springs == "":
			return 1 if len(rules) == 0 else 0
		if springs[0] == '#':
			return solve(Mode.match_hash, springs, rules)
		if springs[0] == '?' and len(rules) != 0:
			return solve(Mode.match_hash, springs, rules) + solve(Mode.skip_dot, springs[1:], rules)
		return solve(Mode.skip_dot, springs[1:], rules)
	
	if mode == Mode.match_hash:
		if len(rules) == 0:
			return 0
		if rules[0] == 0:
			return solve(Mode.next_rule, springs, rules)
		if (len(springs) == 0):
			return 0
		if springs[0] == '.':
			return 0
		rules = (rules[0] - 1,) + rules[1:]
		return solve(Mode.match_hash, springs[1:], rules)

numbers = []

for line in file:
	springs,rules = line.split()
	newsprings = "?".join(([springs] * 5))
	rules = [int(i) for i in rules.split(',')]
	newrules = tuple(rules * 5)
	sol = solve(Mode.skip_dot, newsprings, newrules)
	numbers.append(sol)
	print(springs, rules, sol)
print(sum(numbers))


