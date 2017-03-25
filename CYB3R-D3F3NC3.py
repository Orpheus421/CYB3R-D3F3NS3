
import pygame as pg

pg.init()
screen = pg.display.set_mode((300, 250), pg.RESIZABLE)
done = False
resize_it=False
x = 30
y = 30

clock = pg.time.Clock()

while not done:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			done = True
		elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
			is_blue = not is_blue
		elif event.type == pg.VIDEORESIZE:
			resize_it = True
			new_size= event.size
			screen=pg.display.set_mode((new_size), pg.RESIZABLE)
	
#	if resize_it:
#		w, h = pg..get_surface().get_size()
#		print(str(w)+","+str(h))
		resize_it = False
	
	pressed = pg.key.get_pressed()
	if pressed[pg.K_UP]: y -= 10
	if pressed[pg.K_DOWN]: y += 10
	if pressed[pg.K_LEFT]: x -= 10
	if pressed[pg.K_RIGHT]: x += 10
	
	screen.fill((0, 0, 0))
	color = (0, 128, 255)
	pg.draw.rect(screen, color, pg.Rect(x, y, 60, 60))
	
	pg.display.flip()
	clock.tick(60)
