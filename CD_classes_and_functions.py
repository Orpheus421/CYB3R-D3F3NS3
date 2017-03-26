import pygame as pg
import random as rdm

# Scaling screen function
def scale_and_new_coords(map):
	w, h = pg.display.get_surface().get_size()
	screen_w, screen_h=(w, h)
	x = y = 0
	if (w*9)>(h*16):
		screen_w=int(h*16/9)
		x=int((w-screen_w)/2)
	elif (w*9)<(h*16):
		screen_h=int((w*9/16))
		y=int((h-screen_h)/2)
	scaled_map=pg.transform.smoothscale(map, (screen_w, screen_h))
	scaled_map.convert()
	return (scaled_map, x, y, screen_w, screen_h)

def random_color(flag):
	color=(int(rdm.random()*2)*255, int(rdm.random()*2)*255, int(rdm.random()*2)*255)
	if (color != (0,0,0)) and (color != (255, 255, 255)):
		return color
	elif (flag>5):
		return (218,165,32)
	else:
		return random_color(flag+1)
	
#Enemy class
class Enemy:
	def __init__(self, position, color):
		self.x, self.y = position 
		self.col = color
	
	def move(self):
		if self.y < .22:
			self.y += .001
		elif self.x < 0.8 and self.y < .4:
			self.x += .001
		elif self.y < .5:
			self.y += .001
		elif self.x > .06 and self.y < .7:
			self.x -= .001
		elif self.y < .75 and self.x < 0.1:
			self.y += .001
		elif self.x < 0.8:
			self.x += .001
		else:
			return 1
		return 0
		
	def get_Color(self):
		return self.col
		
	def display(self, screen, x, y, w, h, enemy_size):
				pg.draw.rect(screen, self.col, 
				((self.x*w)+x, (self.y*h)+y, enemy_size, enemy_size))