import pygame as pg

pg.init()
screen = pg.display.set_mode((1200, 700), pg.RESIZABLE)
done = False
resize_it=False
x = 30
y = 30

clock = pg.time.Clock()

while not done:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			done = True
			if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
				is_blue = not is_blue
			if event.type == pg.VIDEORESIZE:
				resize_it == True
	
	if resize_it:
		pass
		# Insert resizing code here
	
	pressed = pg.key.get_pressed()
	if pressed[pg.K_UP]: y -= 3
	if pressed[pg.K_DOWN]: y += 3
	if pressed[pg.K_LEFT]: x -= 3
	if pressed[pg.K_RIGHT]: x += 3
	
	screen.fill((0, 0, 0))
	color = (0, 128, 255)
	pg.draw.rect(screen, color, pg.Rect(x, y, 60, 60))
	
	pg.display.flip()
	clock.tick(60)