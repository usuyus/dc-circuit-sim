import pygame as pg

from graph import Graph
from consts import *

class App:
	def __init__(self, size = (960, 600), title = "dc circuit sim"):
		self.size = self.width, self.height = size
		self.title = title
		self.is_running = True
		self.graph = Graph()

		self.init_pg()
	
	def init_pg(self):
		pg.init()
		self.window = pg.display.set_mode(self.size)
		pg.display.set_caption(self.title)
	
	def handle_event(self, event):
		if event.type == pg.QUIT:
			self.is_running = False
		
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_r:
				mouse_pos = pg.mouse.get_pos()
				self.graph.add_component(DEFAULT_RESISTOR, mouse_pos)
		
		elif event.type == pg.MOUSEBUTTONDOWN:
			pass

	
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
		
		self.cleanup()