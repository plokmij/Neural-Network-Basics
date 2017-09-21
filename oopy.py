#Testing OOP in Python
class Person:
	def __init__(self, name):
		self.name = name
	def greet(self):
		print("Hello ",self.name)

p = Person('Samfan')
p.greet();