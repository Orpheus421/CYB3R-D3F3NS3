import pygame as pg
from CD_classes_and_functions import *
import random as rdm

# Official Shade of Green: "0fc007"

# Pygame initiation
pg.init()
screen = pg.display.set_mode((1200, 700), pg.RESIZABLE)

# Logo and Title
pg.display.set_caption("CYB3R-D3F3NS3")
logo=pg.image.load("C-D_logo.png")
pg.display.set_icon(logo)

done = False

clock = pg.time.Clock()

map=pg.image.load("map.png")
scaled_map, x, y, w, h =scale_and_new_coords(map)
enemy_size=int(0.06*h)
screen.fill((0, 0, 0))

enemies=[]
cooldown=0

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
			enemy_size=int(0.06*h)
	
	screen.blit(scaled_map, (x,y))
	
	cooldown -=1
	
	num=int(rdm.random()*100)
	if num<2 and cooldown<0:
		color=random_color(0)
		if num: position=(0.6, -0.08)
		else: position=(-0.08, 0.25)
		new_enemy=Enemy(position, color)
		enemies.append(new_enemy)
		cooldown=30
	
	for manny in enemies:
		dead = manny.move()
		if dead:
			enemies.remove(manny)
		manny.display(screen, x, y, w, h, enemy_size)
		
	if x:
		pg.draw.rect(screen, (0,0,0),(0, 0, x, h))
		pg.draw.rect(screen, (0,0,0),(w+x, 0, w+2*x, h))
	elif y:
		pg.draw.rect(screen, (0,0,0),(0, 0, w, y))
		pg.draw.rect(screen, (0,0,0),(0, h+y, w, h+2*y))
	
	pg.display.flip()
	clock.tick(60)