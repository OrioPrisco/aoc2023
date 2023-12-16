file = open("input")
import copy

#lasers
Up    = 1 << 0
Left  = 1 << 1
Down  = 1 << 2
Right = 1 << 3
#tiles
Mirror1   = 1 << 4 # \
Mirror2   = 1 << 5 # /
Splitter1 = 1 << 6 # |
Splitter2 = 1 << 7 # -
Nothing   = 1 << 8

beam_mask = 0b000001111
tile_mask = 0b111110000

ascii_to_int = {
	'\\' : Mirror1,
	'/'  : Mirror2,
	'|'  : Splitter1,
	'-'  : Splitter2,
	'.'  : Nothing,
}

int_to_dir = {
	Up    : ( 0,-1),
	Left  : (-1, 0),
	Down  : ( 0, 1),
	Right : ( 1, 0),
}

reflection = {
	ascii_to_int['\\'] :
	{
		Up    : [Left],
		Left  : [Up],
		Down  : [Right],
		Right : [Down],
	},
	ascii_to_int['/']  : 
	{
		Up    : [Right],
		Left  : [Down],
		Down  : [Left],
		Right : [Up],
	},
	ascii_to_int['|']  : 
	{
		Up    : [Up],
		Left  : [Up, Down],
		Down  : [Down],
		Right : [Up, Down],
	},
	ascii_to_int['-']  : 
	{
		Up    : [Left, Right],
		Left  : [Left],
		Down  : [Left, Right],
		Right : [Right],
	},
	ascii_to_int['.']  : 
	{
		Up    : [Up],
		Left  : [Left],
		Down  : [Down],
		Right : [Right],
	},
}

field = [[ascii_to_int[char] for char in line[:-1]] for line in file]
def beam(x,y,direction, field):
	while True:
		if x < 0 or x >= len(field[0]):
			return
		if y < 0 or y >= len(field):
			return
		if field[y][x] & direction:
			return
		field[y][x] |= direction
		new_dirs = reflection[field[y][x] & tile_mask][direction]
		if len(new_dirs) == 1:
			a,b = int_to_dir[new_dirs[0]]
			x += a
			y += b
			direction = new_dirs[0]
			continue
		else:
			for dire in new_dirs:
				beam(x,y, dire, field)
			return

def try_beam_dir(x,y, dire):
	f = copy.deepcopy(field)
	beam(x,y, dire, f)
	total = 0
	for line in f:
		for cell in line:
			if cell & beam_mask:
				total += 1
	print(total)
	return total

best = 0

for x in range(len(field[0])):
	best = max(best, try_beam_dir(x, 0, Down))
	best = max(best, try_beam_dir(x, len(field) - 1, Up))

for y in range(len(field)):
	best = max(best, try_beam_dir(0, y, Right))
	best = max(best, try_beam_dir(len(field[0]) - 1, y, Left))

print(best)
