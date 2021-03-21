from enum import Enum

class CompType(Enum):
	RESISTOR = 0,
	VOLTAGE_SOURCE = 1,
	CURRENT_SOURCE = 2

class Component:
	def __init__(self, type, val):
		self.type = type
		self.val = val

# these are practically just aliases to calling Component
# (doing Component(CompType.RESISTOR, 330) is too clunky :/)

class Resistor(Component):
	type = CompType.RESISTOR
	def __init__(self, val):
		super().__init__(self.type, val)

class VoltageSource(Component):
	type = CompType.VOLTAGE_SOURCE
	def __init__(self, val):
		super().__init__(self.type, val)

class CurrentSource(Component):
	type = CompType.CURRENT_SOURCE
	def __init__(self, val):
		super().__init__(self.type, val)

class Wire(Resistor):
	val = 0
	def __init__(self):
		super().__init__(self.val)
	
	def draw(self, window):
		pass