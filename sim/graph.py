import pygame as pg

from component import Component
from consts import *
from node import Node
from edge import Edge

class Graph:
	def __init__(self):
		self.nodes = []
		self.edges = []
	
	def fill_nodes_until(self, node):
		while len(self.nodes) <= node:
			self.append_node()
	
	def append_node(self, pos = (0, 0)):
		self.nodes.append(Node(len(self.nodes), pos))
	
	def add_component(self, comp, pos):
		x, y = pos
		self.append_node((x-DEFAULT_EDGE_LENGTH//2, y))
		self.append_node((x+DEFAULT_EDGE_LENGTH//2, y))

		last = len(self.nodes) - 1
		self.add_edge(comp, last-1, last)
	
	def add_edge(self, comp, u, v):
		self.fill_nodes_until(max(u, v))

		edge = Edge(self.nodes[u], self.nodes[v], comp, len(self.edges))
		self.edges.append(edge)

		self.nodes[u].add_edge(edge)
		self.nodes[v].add_edge(edge)
	
	def remove_edge(self, idx):
		assert len(self.edges) > idx # can't remove a non-existing edge

		edge = self.edges[idx]
		edge.src.remove_edge(edge)
		edge.dest.remove_edge(edge)

		del self.edges[idx]
		reindex(self.edges)
	
	def merge_nodes(self, u, v):
		assert len(self.nodes) > max(u, v) # can't merge non-exsiting nodes

		self.nodes[u].merge_with(self.nodes[v])
		del self.nodes[v]
		reindex(self.nodes)
	
	def draw(self, window):
		for edge in self.edges: edge.draw(window)
		for node in self.nodes: node.draw(window)

def reindex(arr):
	for a, i in zip(arr, range(len(arr))):
		a.idx = i