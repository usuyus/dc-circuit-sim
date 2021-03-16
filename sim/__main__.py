from graph import Graph
from component import Component, CompType

def main():
	G = Graph()
	
	V = Component(CompType.VOLTAGE_SOURCE, 5)
	R1 = Component(CompType.RESISTOR, 330)
	R2 = Component(CompType.RESISTOR, 1000)

	G.add_edge(V, 0, 1)
	G.add_edge(R1, 1, 2)
	G.add_edge(R2, 2, 0)

if __name__ == "__main__":
	main()
