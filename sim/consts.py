import pygame as pg

from component import Component, CompType

BLACK = 0, 0, 0
WHITE = 255, 255, 255
DEFAULT_RESISTOR = Component(CompType.RESISTOR, 330)

pg.font.init()
DEFAULT_FONT = pg.font.Font(pg.font.get_default_font(), 20)

DEFAULT_EDGE_LENGTH = 120

NODE_SIZE = 15
NODE_THICKNESS = 1