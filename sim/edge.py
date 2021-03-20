import pygame as pg
import math

from consts import *
from utils import *

class Edge:
	def __init__(self, src, dest, comp, idx = None):
		self.idx = idx
		self.src = src
		self.dest = dest
		self.comp = comp
	
	def draw(self, window):
		x1, y1 = self.src.pos
		x2, y2 = self.dest.pos
		l = dist((x1, y1), (x2, y2))

		if l <= 2 * NODE_SIZE: return

		# for the line to not go into the nodes
		dx, dy = (x2-x1) / l, (y2-y1) / l
		x1 += dx * NODE_SIZE
		y1 += dy * NODE_SIZE
		x2 -= dx * NODE_SIZE
		y2 -= dy * NODE_SIZE

		pg.draw.line(window, WHITE, (x1, y1), (x2, y2), 3)

