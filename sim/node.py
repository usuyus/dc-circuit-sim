import pygame as pg

from consts import *
from utils import *

class Node:
	def __init__(self, idx = None, pos = (0, 0)):
		self.idx = idx
		self.pos = pos
		self.in_edges = []
		self.out_edges = []
	
	def add_edge(self, edge):
		if edge.src is self: self.out_edges.append(edge)
		if edge.dest is self: self.in_edges.append(edge)
	
	def remove_edge(self, edge):
		self.in_edges[:] = (e for e in self.in_edges if e is not edge)
		self.out_edges[:] = (e for e in self.out_edges if e is not edge)
	
	def merge_with(self, node):
		vis = set(self.in_edges)
		
		for e in node.in_edges:
			e.dest = self
			if e not in vis: self.in_edges.append(e)
			vis.add(e)
		
		vis = set(self.out_edges)
		
		for e in node.out_edges:
			e.src = self
			if e not in vis: self.out_edges.append(e)
			vis.add(e)
	
	def is_near(self, p):
		return dist(self.pos, p) <= NODE_SIZE
	
	def draw(self, window):
		pg.draw.circle(window, WHITE, self.pos, NODE_SIZE, NODE_THICKNESS)

		label = DEFAULT_FONT.render(str(self.idx), True, WHITE)
		label_rect = label.get_rect(center = self.pos)
		window.blit(label, label_rect)