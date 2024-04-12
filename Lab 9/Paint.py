import pygame
import sys

pygame.init()
#устанавливаем размеры окна и панели
height = 600
panel_height = 100
width = 800
#создаем окно и поверхности 
window = pygame.display.set_mode((width, height))
screen = pygame.Surface((width, height - panel_height))
another_layer = pygame.Surface((width, height - panel_height))
panel = pygame.Surface((width, panel_height))

queue = []
#функция для создания различных фигур
def getRectangle(x1, y1, x2, y2):
        x = min(x1, x2)
        y = min(y1, y2)
        w = abs(x1-x2)
        h = abs(y1-y2)
        return (x, y, w, h)

def getSquare(x1, y1, x2, y2):
    w = abs(x1-x2)
    h = abs(y1-y2)
    w = min(w, h)
    if x1 < x2:
        x = x1
    else:
        x = x1 - w
    if y1 < y2:
        y = y1
    else:
        y = y1 - w
    return(x, y, w, w)

def getRadius(x1, y1, x2, y2):
    r = max(abs(x1-x2), abs(y1-y2))
    return r

# Функция для заполнения области
def step(screen, x, y, origin_color, fill_color):
    if x < 0 or y < 0: return False
    if x > width-1 or y > height-panel_height-1: return False
    if screen.get_at((x, y)) != origin_color: return False
    queue.append((x, y))
    screen.set_at((x, y), fill_color)

## Загружаем изображения инструментов

pencil = pygame.image.load('pencil.png')
pencil = pygame.transform.scale(pencil, (75, 75))
rect = pencil.get_rect()
rect1 = rect.move(10, 10)
rect2 = rect.move(95, 10)
rect3 = rect.move(180, 10)
rect4 = rect.move(265, 10)
rect5 = rect.move(350, 10)
rect6 = rect.move(435, 10)
rect7 = rect.move(520, 10)
rect8 = rect.move(605, 10)

bucket = pygame.image.load('bucket.png')
bucket = pygame.transform.scale(bucket, (75, 75))

eraser = pygame.image.load('eraser.png')
eraser = pygame.transform.scale(eraser, (75, 75))

figures = pygame.image.load('figures.png')
figures = pygame.transform.scale(figures, (75, 75))

#устанавливаем цвета

BLACK = (0, 0, 0)
DARK_GRAY = (50, 50, 50)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 100, 0)
VIOLETE = (128, 0, 128)

COLOR = BLUE

fill_color = COLOR

mouse_pressed = False

tool = 0
tools = 4

screen.fill(BLACK)

poligons = False
colors = False