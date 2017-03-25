import pygame as pg
from CD_classes_and_functions import *

# Official Shade of Green: "0fc007"

# Pygame initiation
pg.init()
screen = pg.display.set_mode((1200, 700), pg.RESIZABLE)

# Logo and Title
pg.display.set_caption("CYB3R-D3F3NS3")
logo=pg.image.load("C-D_logo.png")
pg.display.set_icon(logo)

done = False

# DELETE EVENTUALLY

box_x = 30
box_y = 30

# !!

clock = pg.time.Clock()

map=pg.image.load("map.png")
scaled_map, x, y, w, h =scale_and_new_coords(map)
screen.fill((0, 0, 0))

while not done:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			done = True
#		How to detect if a key is pressed
#		if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
		if event.type == pg.VIDEORESIZE:
			new_size= event.size
			screen=pg.display.set_mode((new_size), pg.RESIZABLE)
			scaled_map, x, y, w, h =scale_and_new_coords(map)
	
# DELTE EVENTUALLY
	pressed = pg.key.get_pressed()
	if pressed[pg.K_UP]: box_y -= 3
	if pressed[pg.K_DOWN]: box_y += 3
	if pressed[pg.K_LEFT]: box_x -= 3
	if pressed[pg.K_RIGHT]: box_x += 3
# !!
	
	screen.blit(scaled_map, (x,y))

	pg.draw.rect(screen, (0, 128, 255), pg.Rect(box_x, box_y, 60, 60))
	
	pg.display.flip()
	clock.tick(60)