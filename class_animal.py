class Animal():
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		self.sound = 'none'

	def feed(self):
		print(self.name + ' feeded')

class Milking(Animal):
	def milk(self):
		print(self.name + ' milked')

class Oviparous(Animal):
	def collect_eggs(self):
		print(self.name + " egg's collected")

class Goose(Oviparous):
	def __init__(self, name, weight):
		super().__init__(name, weight)
		self.sound = 'honk'

class Cow(Milking):
	def __init__(self, name, weight):
		super().__init__(name, weight)
		self.sound = 'moo'

class Sheep(Animal):
	def __init__(self, name, weight):
		super().__init__(name, weight)
		self.sound = 'baa'

	def shear(self):
		print(self.name + ' sheared')

class Hen(Oviparous):
	def __init__(self, name, weight):
		super().__init__(name, weight)
		self.sound = 'cluck'

class Goat(Milking):
	def __init__(self, name, weight):
		super().__init__(name, weight)
		self.sound = 'bleat'

class Duck(Oviparous):
	def __init__(self, name, weight):
		super().__init__(name, weight)
		self.sound = 'quack'

if __name__ == '__main__':
	animals = []
	animals.append(Goose('Gray', 32))
	animals.append(Goose('White', 34))
	animals.append(Cow('Manka', 300))
	animals.append(Sheep('Lamb', 70))
	animals.append(Sheep('Curly', 72))
	animals.append(Hen('Ko-ko', 3))
	animals.append(Hen('Cock-A-Doodle-Doo', 4))
	animals.append(Goat('Horns', 60))
	animals.append(Goat('Hooves', 64))
	animals.append(Duck('Mallard', 42))

	sm_weight = 0
	mx_weight = 0
	mx_animal = None
	for a in animals:
		print(a.name + ' has sound ' + a.sound)
		a.feed()
		if isinstance(a, Milking):
			a.milk()
		if isinstance(a, Oviparous):
			a.collect_eggs()
		sm_weight += a.weight
		if a.weight > mx_weight:
			mx_weight = a.weight
			mx_animal = a
	print('Total weight:', sm_weight)
	print('Max weight:', mx_weight, 'of animal', mx_animal.name)



        
        
        
        

        
                
