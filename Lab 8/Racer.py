import pygame as pg
import datetime as dt
import random 

pg.init()

size = [500, 600]
center = [250, 300]
screen = pg.display.set_mode(size)
clock = pg.time.Clock()

road_color = 20, 20, 20
enemy_color = 200, 10, 40
player_color = 40, 10, 200
grass_color = 0, 150, 0
bordur_color = 255, 255, 255
line_color = 255, 255, 0

grass_rect = pg.Rect(0, 0, 60, 600)
grass_rect1 = pg.Rect(440, 0, 60, 600)
bordur_rect = pg.Rect(60, 0, 5, 600)
bordur_rect1 = pg.Rect(435, 0, 5, 600)

pg.display.set_caption("Racer")

W = 40
L = 70

liney = -600
liney1 = 0

playerx = 210
playery = 400

enemyx= random.randint(70, 390)
enemyy= -70
##Диапазон движения машин от 70 до 390

def car_draw(X, Y, W, L, car_color):
    car_rect = pg.Rect(X, Y, W, L)
    pg.draw.rect(screen, car_color,car_rect)

def line_draw(X, Y, W, L, line_color):
    line_rect1 = pg.Rect(X, Y, W, L)
    pg.draw.rect(screen, line_color, line_rect1)
    line_rect2 = pg.Rect(X, Y+40, W, L)
    pg.draw.rect(screen, line_color, line_rect2)
    line_rect3 = pg.Rect(X, Y+80, W, L)
    pg.draw.rect(screen, line_color, line_rect3)
    line_rect4 = pg.Rect(X, Y+120, W, L)
    pg.draw.rect(screen, line_color, line_rect4)
    line_rect5 = pg.Rect(X, Y+160, W, L)
    pg.draw.rect(screen, line_color, line_rect5)
    line_rect6 = pg.Rect(X, Y+200, W, L)
    pg.draw.rect(screen, line_color, line_rect6)
    line_rect11 = pg.Rect(X, Y+240, W, L)
    pg.draw.rect(screen, line_color, line_rect11)
    line_rect22 = pg.Rect(X, Y+280, W, L)
    pg.draw.rect(screen, line_color, line_rect22)
    line_rect33 = pg.Rect(X, Y+320, W, L)
    pg.draw.rect(screen, line_color, line_rect33)
    line_rect44 = pg.Rect(X, Y+360, W, L)
    pg.draw.rect(screen, line_color, line_rect44)
    line_rect55 = pg.Rect(X, Y+400, W, L)
    pg.draw.rect(screen, line_color, line_rect55)
    line_rect66 = pg.Rect(X, Y+440, W, L)
    pg.draw.rect(screen, line_color, line_rect66)
    line_rect33 = pg.Rect(X, Y+480, W, L)
    pg.draw.rect(screen, line_color, line_rect33)
    line_rect44 = pg.Rect(X, Y+520, W, L)
    pg.draw.rect(screen, line_color, line_rect44)
    line_rect55 = pg.Rect(X, Y+560, W, L)
    pg.draw.rect(screen, line_color, line_rect55)
    line_rect66 = pg.Rect(X, Y+600, W, L)
    pg.draw.rect(screen, line_color, line_rect66)

running = True
while running:
    screen.fill(road_color)
    pg.draw.rect(screen, bordur_color, bordur_rect)
    pg.draw.rect(screen, bordur_color, bordur_rect1)
    pg.draw.rect(screen, grass_color, grass_rect)
    pg.draw.rect(screen, grass_color, grass_rect1)
    if(playerx in range (enemyx-40, enemyx+40) and playery in range (enemyy-70,enemyy+70)):
       print("You dead")
       running = False
       
    else:
        line_draw(245, liney1, 5, 30, line_color)
        line_draw(245, liney, 5, 30, line_color)
        car_draw(playerx, playery, W, L, player_color)
        car_draw(enemyx, enemyy, W, L, enemy_color)

    liney+=5
    liney1+=5
    if(liney == 0): liney = -600
    if(liney1 == 600): liney1= 0


    enemyy+=5
    if(enemyy==670): 
        enemyx= random.randint(70, 390)
        enemyy=-70
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        if(playerx > 70): playerx-=4
    if keys[pg.K_RIGHT]:
        if(playerx < 390): playerx+=3
    if keys[pg.K_UP]:
        if(playery > 200): playery-=3
    if keys[pg.K_DOWN]:
        if(playery < 500): playery+=2
    pg.display.flip()
    clock.tick(30)

pg.quit()