from enum import Enum

class CompType(Enum):
	RESISTOR = 0,
	VOLTAGE_SOURCE = 1,
	CURRENT_SOURCE = 2

class Component:
	def __init__(self, type, val):
		self.type = type
		self.val = val