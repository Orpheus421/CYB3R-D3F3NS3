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
	
#Enemy class
class Enemy:
	def __init__(self,position,color)
		self.pos = positon 
		self.col = color
	
	def string(self):
		if self.pos[1] < .22:
			self.pos[1]+.05
		elif self.pos[0] < 0.8 and self.pos[1] < .4:
			self.pos[0] + .05
		elif self.pos[1] < .5:
			self.pos[1] + .05
		elif self.pos[0] > .06 and self.pos[1] < .7:
			self.pos[0] - .05
		elif self.pos[1] < .75:
			self.pos[1] + .05
		elif self.pos[0] < 0.8:
			self.pos[0] + .05
		else:
			eself.pos[0]it()
		return self.pos
		
