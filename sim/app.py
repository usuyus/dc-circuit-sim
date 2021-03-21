import pygame as pg

from graph import Graph
from component import *
from consts import *

class App:
	def __init__(self, size = (960, 600), title = "dc circuit sim"):
		self.size = self.width, self.height = size
		self.title = title
		self.is_running = True
		self.graph = Graph()

		self.dragged = None # can only be a node for now

		self.init_pg()
	
	def load_resources(self):
		self.resources = {}
		self.resources["VOLTAGE_SOURCE"] = pg.image.load("res/voltage_source.png")
	
	def init_pg(self):
		pg.init()
		self.load_resources()
		
		self.window = pg.display.set_mode(self.size, vsync=1)
		pg.display.set_caption(self.title)
		pg.display.set_icon(self.resources["VOLTAGE_SOURCE"])
	
	def handle_event(self, event):
		if event.type == pg.QUIT:
			self.is_running = False
		
		elif event.type == pg.KEYDOWN:
			mouse_pos = pg.mouse.get_pos()
			
			if event.key == pg.K_w: # wire
				self.graph.add_component(Resistor(0), mouse_pos)
			
			elif event.key == pg.K_r: # resistor	
				self.graph.add_component(Resistor(330), mouse_pos)
		
		elif event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1: # left click
				self.begin_drag(event.pos)
		
		elif event.type == pg.MOUSEMOTION:
			self.update_drag(event.pos)
		
		elif event.type == pg.MOUSEBUTTONUP:
			if event.button == 1: # left click
				self.end_drag()

	def begin_drag(self, mouse_pos):
		for node in self.graph.nodes:
			if node.is_near(mouse_pos):
				self.dragged = node
				return True
		
		return False
	
	def update_drag(self, mouse_pos):
		if self.dragged is not None:
			self.dragged.pos = mouse_pos
	
	def end_drag(self):
		if self.dragged is None: return False
		
		for node in self.graph.nodes:
			if node is not self.dragged and node.is_near(self.dragged.pos):
				self.graph.merge_nodes(node.idx, self.dragged.idx)
				break
		
		self.dragged = None
		return True
	
	def update(self):
		pass
	
	def render(self):
		self.window.fill(BLACK)

		self.graph.draw(self.window)

		pg.display.flip()
	
	def cleanup(self):
		pg.quit()

	def run(self):
		while self.is_running:
			for event in pg.event.get():
				self.handle_event(event)
			
			self.update()
			self.render()
			pg.time.wait(1) # for lowering cpu usage, idk whether it actually works tho
		
		self.cleanup()