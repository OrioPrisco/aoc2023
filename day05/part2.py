file = open("input")


def get_map(file):
	file.readline()
	file.readline()
	result = []
	while (line := file.readline()).strip():
		print(line)
		result.append([int(i) for i in line.split()])
	return result

def convert_r(r, maps, recurse):
	unconverted = []
	results = []
	result = range(0)
	for map in maps:
		if r.start < map[1] <= r.stop:
			unconverted.append(range(r.start, map[1]))
			r = range(map[1], r.stop)
		if r.start < map[1] + map[2] <= r.stop:
			unconverted.append(range(map[1] + map[2], r.stop))
			r = range(r.start, map[1] + map[2])
		if r.start >= map[1] and r.stop <= map[1] + map[2]:
			result = range(r.start + map[0] - map[1], r.stop + map[0] - map[1])
	if (result.start != result.stop):
		results.append(result)
	if recurse > 0:
		results += convert_rs(unconverted, maps, recurse - 1)
	else:
		results += unconverted
	return results


def convert_rs(rs, maps, recurse = 10):
	result = []
	for r in rs:
		print(f"r {r}")
		if r.start == r.stop:
			continue
		result += convert_r(r, maps, recurse)
	return result

def solve():
	seeds = [int(i) for i in file.readline().split(":")[1].split()]
	seed_ranges = [range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
	seed_to_soil = get_map(file)
	soil_to_fertilizer = get_map(file)
	fertilizer_to_water = get_map(file)
	water_to_light = get_map(file)
	light_to_temperature = get_map(file)
	temperature_to_humidity = get_map(file)
	humidity_to_location = get_map(file)
	
	soils = convert_rs(seed_ranges, seed_to_soil)
	fertilizers = convert_rs(soils, soil_to_fertilizer)
	waters = convert_rs(fertilizers, fertilizer_to_water)
	lights = convert_rs(waters, water_to_light)
	temperatures = convert_rs(lights, light_to_temperature)
	humiditys = convert_rs(temperatures, temperature_to_humidity)
	locations = convert_rs(humiditys, humidity_to_location)
	out_ranges = []
	#print(f"Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}.")
	for i in locations:
		print(i)
		if i.start != i.stop:
			out_ranges.append(i)
	print(min([min(i) for i in out_ranges]))

solve()
