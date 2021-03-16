from component import Component

class Node:
	def __init__(self, idx = None):
		self.idx = idx
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

class Edge:
	def __init__(self, src, dest, comp, idx = None):
		self.idx = idx
		self.src = src
		self.dest = dest
		self.comp = comp

class Graph:
	def __init__(self):
		self.nodes = []
		self.edges = []
	
	def fill_nodes_until(self, node):
		while len(self.nodes) <= node:
			self.append_node()
	
	def append_node(self):
		self.nodes.append(Node(len(self.nodes)))
	
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

def reindex(arr):
	for a, i in zip(arr, range(len(arr))):
		a.idx = i