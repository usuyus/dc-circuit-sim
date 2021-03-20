import math

def dist(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return math.hypot(x1 - x2, y1 - y2)