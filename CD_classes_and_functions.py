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
	
#Enemy class
class Enemy:
	def __init__(self, position, color):
		self.x, self.y = position 
		self.col = color
	
	def move(self):
		if self.y < .195:
			self.y += .001
		elif self.x < 0.61 and self.y < .4:
			self.x += .001
		elif self.y < .475:
			self.y += .001
		elif self.x > .115 and self.y < .7:
			self.x -= .001
		elif self.y < .75 and self.x < 0.15:
			self.y += .001
		elif self.x < 0.761:
			self.x += .001
		else:
			return 1
		return 0
		
	def get_Color(self):
		return self.col
		
	def display(self, screen, x, y, w, h, enemy_size):
				pg.draw.rect(screen, self.col, 
				((self.x*w)+x, (self.y*h)+y, enemy_size, enemy_size))
			
# NEEDS HEAVY EDITING
class Slots:
	def __init__ (self, position1, position2, size1, size2):
		self.empty = Button(position1, size1, 1, "empty")
		self.buy = Button(position2, size2, 1, "buy")
		self.tower1 = Button(position1, size1, 0, "tower1")
		self.upgrade = Button(position2, size2, 0, "upgrade")
		self.tower2 = Button(position1, size1, 0, "tower2")
		
	def display(self, screen, x, y, w, h):
		if self.empty.visible:
			self.empty.display(screen, x, y, w, h)
			if self.buy.visible:
				self.buy.display(screen, x, y, w, h)
		elif self.tower1.visible:
			self.tower1.display(screen, x, y, w, h)
			if self.upgrade.visible: 
				self.upgrade.display(screen, x, y, w, h)
		else:
			self.tower2.display(screen, x, y, w, h)

class Button:
	def __init__ (self,position,size,visible,type):
		self.x = position[0]
		self.y = position[1]
		self.h = size[0]
		self.w = size[1]
		self.visible = visible
		self.type = type
		
		if self.type == "empty":
			self.color=(192, 192, 192)
		elif self.type == "buy":
			self.color=(0, 255, 0)
		elif self.type == "tower1":
			self.color=(0, 128, 128)
		elif self.type == "upgrade":
			self.color=(0, 255, 0)
		else:
			self.color=(0, 0, 128)
		
	def display(self, screen, x, y, w, h):
		pg.draw.ellipse(screen, self.color, 
		((self.x*w)+x, (self.y*h)+y, int(self.h*h), int(self.w*h)))