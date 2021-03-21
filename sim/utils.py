import math
import pygame as pg

def dist(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return math.hypot(x1 - x2, y1 - y2)

def rotate_center(img, angle, x, y):
	res_img = pg.transform.rotate(img, angle)
	res_rect = res_img.get_rect(
		center = img.get_rect(center = (x, y)).center
	)

	return res_img, res_rect