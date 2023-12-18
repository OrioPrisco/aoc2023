file = open("input")

s_pos = (0, 0)

dir_to_coord = {
	"3" : ( 0, -1),
	"1" : ( 0,  1),
	"0" : ( 1,  0),
	"2" : (-1,  0),
}

def add_coord(a,b):
	return (a[0] + b[0], a[1] + b[1])

def mult_coord(c, a):
	return (c[0] * a, c[1] * a)

instructions = [line.split() for line in file]

p = [(0,0)]
perimeter = 0

for instruction in instructions:
	direction, number, color = instruction
	direction = color[-2]
	number = int(color[2:-2], 16)
	print(number)
	perimeter += number
	s_pos = add_coord(s_pos, mult_coord(dir_to_coord[direction], number))
	p.append(s_pos)

def area(p):
	return 0.5 * abs(sum(x0*y1 - x1*y0 for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
	return zip(p, p[1:] + [p[0]])

#helf of perimeter is because coordinates are halway inside the perimeter blocks
# no clue why the 1 is needed
print(area(p) + 1 + perimeter / 2)
