import pygame as pg
import datetime
pg.init()
size = [500, 500]
screen = pg.display.set_mode(size)
clock = pg.time.Clock()

XC = 250
YC = 250
cords = [XC, YC]

fill_color = 255, 255, 255
circle_color = 255, 0 , 0

running = True
while running:

    screen.fill(fill_color)
    pg.draw.circle(screen, circle_color, (XC, YC), 20)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                if(YC > 40): YC-=20
            if event.key == pg.K_DOWN:
                if(YC < 460): YC+=20
            if event.key == pg.K_RIGHT:
                if(XC < 460): XC+=20
            if event.key == pg.K_LEFT:
                if(XC > 40): XC-=20
    pg.display.flip()
    clock.tick(30)

pg.quit()