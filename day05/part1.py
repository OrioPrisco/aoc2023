file = open("input")


def get_map(file):
	file.readline()
	file.readline()
	result = []
	while (line := file.readline()).strip():
		print(line)
		result.append([int(i) for i in line.split()])
	return result

def convert(value, maps):
	for map in maps:
		if value in range(map[1], map[1] + map[2]):
			return map[0] + value - map[1]
	return value

numbers = []
seeds = [int(i) for i in file.readline().split(":")[1].split()]
seed_to_soil = get_map(file)
soil_to_fertilizer = get_map(file)
fertilizer_to_water = get_map(file)
water_to_light = get_map(file)
light_to_temperature = get_map(file)
temperature_to_humidity = get_map(file)
humidity_to_location = get_map(file)

for seed in seeds:
	soil = convert(seed, seed_to_soil)
	fertilizer = convert(soil, soil_to_fertilizer)
	water = convert(fertilizer, fertilizer_to_water)
	light = convert(water, water_to_light)
	temperature = convert(light, light_to_temperature)
	humidity = convert(temperature, temperature_to_humidity)
	location = convert(humidity, humidity_to_location)
	numbers.append(location)
	print(f"Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}.")

print(min(numbers))

