import pygame as pg

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
	
	
def in_range(x, y, w, h, button_position, button_size, cursor_position):
	return (cursor_position[0]>(button_position[0]*w+x) and cursor_position[0]<((button_position[0]+button_size[0])*w+x) 
	and cursor_position[1]>(button_position[1]*h+y) and cursor_position[1]<((button_position[1]+button_size[1])*h+y))

#Stats class
class Stats:
	def __init__(self, health=50, gold=25):
		self.hp=health
		self.g=gold
		
	def display(self, my_font):
		health=my_font.render("Health: "+str(self.hp), True, (15, 192, 7))
		gold=my_font.render("Gold: "+str(self.g), True, (15, 192, 7))
		return (health, gold)
	
#Enemy class
class Enemy:
	def __init__(self, position, color):
		self.x, self.y = position 
		self.col = color
	
	def move(self):
		if self.y < .195:
			self.y += .0016
		elif self.x < 0.61 and self.y < .4:
			self.x += .0009
		elif self.y < .475:
			self.y += .0016
		elif self.x > .115 and self.y < .7:
			self.x -= .0009
		elif self.y < .75 and self.x < 0.15:
			self.y += .0016
		elif self.x < 0.761:
			self.x += .0009
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
		self.buy = Button(position2, size2, 0, "buy")
		self.tower1 = Button(position1, size1, 0, "tower1")
		self.upgrade = Button(position2, size2, 0, "upgrade")
		self.tower2 = Button(position1, size1, 0, "tower2")
		self.cooldown = 0
		self.firing_time = 0
		self.enemy=0
		
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
			
	def tower_is_pressed(self, x, y, w, h, cursor_position):
		return in_range(x, y, w, h, (self.empty.x, self.empty.y), 
		(self.empty.h, self.empty.w), cursor_position)
	
	def purchase(self, player):
		if self.empty.visible and player.g>15:
			self.empty.visible=0
			self.tower1.visible=1
			player.g-=15
		elif self.tower1.visible and player.g>30:
			self.tower1.visible=0
			self.tower2.visible=1
			player.g-=30

	def enter_shop(self):
		if self.tower2.visible:
			return False
		elif self.tower1.visible:
			self.upgrade.visible=1
		else:
			self.buy.visible=1
		return True

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