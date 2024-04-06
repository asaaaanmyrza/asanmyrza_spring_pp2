import pygame as pg
import constants as c
pg.init()
screen = pg.display.set_mode(c.size)
clock = pg.time.Clock()
running = True
while running:
    screen.fill(c.white)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()
    clock.tick(30)

pg.quit()