file = open("input")

low = 0
high = 1

class Module:
	def __init__(self, name, kind, params):
		self.name = name
		self.kind = kind
		self.params = [i.strip() for i in params.split(",")]
		if kind == "broadcaster" or kind == "button":
			self.state = None
		if kind == '&':
			self.state = {}
		if kind == '%':
			self.state = low
	def __str__(self):
		return  "Module " + self.kind + self.name
	def __repr__(self):
		return  "Module " + self.kind + self.name
	def dummy_send(self, modules_dict):
		for module_name in self.params:
			if module_name in modules_dict:
				modules_dict[module_name].dummy_receive(self.name)
	def dummy_receive(self, by):
		if self.kind == '&':
			self.state[by] = low
	def fire_low(self):
		return (0, len(self.params),  [(i, low ) for i in self.params])
	def fire_high(self):
		return (len(self.params), 0, [(i, high) for i in self.params])
	#return [high, low, (name, pulse)]
	def fire(self, pulse, by):
		if self.kind == "button":
			return (0,1,[("broadcaster", low)])
		if self.kind == "broadcaster":
			return self.fire_low() if pulse == low else self.fire_high()
		if self.kind == '%':
			if pulse == low:
				self.state = high if self.state == low else low
				return self.fire_low() if self.state == low else self.fire_high()
			return (0,0,[])
		if self.kind == '&':
			self.state[by] = pulse
			return self.fire_low() if all([self.state[i] == high for i in self.state]) else self.fire_high()

modules_list = []
modules_dict = {}

for line in file:
	module,param = line.split("->")
	if module == "broadcaster ":
		name = "broadcaster"
		kind = "broadcaster"
	else:
		name = module[1:-1]
		kind = module[0]
	m = Module(name, kind, param)
	modules_list.append(m)
	modules_dict[name] = m

for module in modules_list:
	module.dummy_send(modules_dict)

total_high = 0
total_low = 0
for i in range(1000):
	to_fire = [("broadcaster", low, "button")]
	total_low += 1 #button send a low pulse
	while len(to_fire):
		name, pulse, by = to_fire.pop(0)
		print(f"{by} -{'low' if pulse == low else 'high'}-> {name}")
		if name in modules_dict:
			high_p, low_p, to_add = modules_dict[name].fire(pulse, by)
			total_high += high_p
			total_low += low_p
			to_fire += [item + (name,) for item in to_add]
	print(f"{i} : {total_high}, {total_low}")
print(total_high * total_low)
