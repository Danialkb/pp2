import pygame as pg
from math import *
pg.init()
screen = pg.display.set_mode((800, 600))
screen.fill((255, 255, 255))
RED = (255, 0, 0)   
GREEN = (0, 255, 0)   
BLUE = (0, 0, 255)   
BLACK = (0, 0, 0)
palitra = pg.image.load('images/pal.png')
d = {
    'rect': False,
    'circle': False,
    'eraser': False,
    'square': False,
    'right_triangle': False,
    'rhombus': False,
    'triangle': False
}

def rectangle(screen, cur, pos, d, color): # функция рисования прямоугольника
    x1, y1, x2, y2 = cur[0], cur[1], pos[0], pos[1]
    side1 = abs(x1-x2)
    side2 = abs(y1-y2)
    if x1 <= x2:
        if y1 < y2:
            pg.draw.rect(screen, color, (x1, y1, side1, side2), d)
        else:
            pg.draw.rect(screen, color, (x1, y2, side1, side2), d)
    else:
        if y1 < y2:
            pg.draw.rect(screen, color, (x2, y1, side1, side2), d)
        else:
            pg.draw.rect(screen, color, (x2, y2, side1, side2), d)

def square(screen, cur, pos, d, color): # функция для квадрата
    x1, y1, x2, y2 = cur[0], cur[1], pos[0], pos[1]

    side1 = abs(x1-x2)
    side2 = side1
    # side2 = abs(y1-y2)

    if x1 <= x2:
        if y1 < y2:
            pg.draw.rect(screen, color, (x1, y1, side1, side2), d)
        else:
            pg.draw.rect(screen, color, (x1, y2, side1, side2), d)
    else:
        if y1 < y2:
            pg.draw.rect(screen, color, (x2, y1, side1, side2), d)
            
        else:
            pg.draw.rect(screen, color, (x2, y2, side1, side2), d)

def right_triangle(screen, cur, pos, d, color):# для прямоугольного тр-ка
    x1, y1, x2, y2 = cur[0], cur[1], pos[0], pos[1]
    difx = abs(x1-x2)
    dify = abs(y1-y2)
    if x1 <= x2:
        if y1 < y2:
            pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 + dify), (x2, y2)], d)   
        else:
            pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 - dify), (x2, y2)], d)   
            
    else:
        if y1 < y2:
            pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 + dify), (x2, y2)], d)   
        else:
            pg.draw.polygon(screen, color, [(x1, y1), (x1, y1 - dify), (x2, y2)], d)   
        

def triangle(screen, posi, d, color): # функция для равностороннего треугольника
    # x1, y1, x2, y2 = cur[0], cur[1], pos[0], pos[1]
    pg.draw.polygon(screen, color,  posi, d)
        
def circle(screen, cur, pos, d, color):
    x1, y1, x2, y2 = cur[0], cur[1], pos[0], pos[1]
    side1 = abs(x1-x2)
    side2 = abs(y1-y2)

    if x1 <= x2:
        if y1 < y2:
            pg.draw.ellipse(screen, color, (x1, y1, side1, side2), d)
        else:
            pg.draw.ellipse(screen, color, (x1, y2, side1, side2), d)
    else:
        if y1 < y2:
            pg.draw.ellipse(screen, color, (x2, y1, side1, side2), d)
        else:
            pg.draw.ellipse(screen, color, (x2, y2, side1, side2), d)

def rhombus(screen, cur, pos, d, color): # функция для ромба
    x1 = cur[0]
    y1 = cur[1]
    x2 = pos[0]
    y2 = pos[1]

    difx = abs(x1-x2)
    dify = abs(y1-y2)

    pg.draw.polygon(screen, color, [(x1, y1), (x1 - difx, y1 + dify//2), (x2, y2), (x1 + 2*difx, y1 + dify//2)], 4)

cur = (0, 0)
t = 3

eraser = False
lastik_size = 50
mycolour = (11, 102, 35) # по умолчанию цвет 'forest green'

running = True

while running:
    pos = pg.mouse.get_pos() # получаю текущую позицию моей мыши
    screen.blit(pg.transform.scale(palitra, (100, 100)), (0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if 0<= pos[0] <= 100 and 0<= pos[1] <= 100:
                mycolour = screen.get_at(pos) # меняю цвет по pal.png
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r: # выбираем прямоугольник
                d['rect'] = True
                for k, v in d.items():
                    if k != 'rect':
                        d[k] = False
            if event.key == pg.K_p: # выбираем правильный треугольник
                d['triangle'] = True
                for k, v in d.items():
                    if k != 'triangle':
                        d[k] = False
            if event.key == pg.K_s: # выбираем square
                d['square'] = True
                for k, v in d.items():
                    if k != 'square':
                        d[k] = False
            if event.key == pg.K_c: # выбираем круг
                d['circle'] = True
                for k, v in d.items():
                    if k != 'circle':
                        d[k] = False
            if event.key == pg.K_t: # выбираем прямоугольный треугольник
                d['right_triangle'] = True
                for k, v in d.items():
                    if k != 'right_triangle':
                        d[k] = False
            if event.key == pg.K_g: # выбираем ромб
                d['rhombus'] = True
                for k, v in d.items():
                    if k != 'rhombus':
                        d[k] = False
            if event.key == pg.K_e: # выбираем ластик
                d['eraser'] = True
                for k, v in d.items():
                    if k != 'eraser':
                        d[k] = False
                    
        if d['rect'] == True:
            if event.type == pg.MOUSEBUTTONDOWN:
                cur = pos 
            if event.type == pg.MOUSEBUTTONUP:
                rectangle(screen, cur, pos, t, mycolour)
        elif d['circle'] == True:
            if event.type == pg.MOUSEBUTTONDOWN:
                cur = pos
            if event.type == pg.MOUSEBUTTONUP:
                circle(screen, cur, pos, t, mycolour)
        elif d['square'] == True:
            if event.type == pg.MOUSEBUTTONDOWN:
                cur = pos
            if event.type == pg.MOUSEBUTTONUP:
                square(screen, cur, pos, t, mycolour)
        elif d['right_triangle'] == True:
            if event.type == pg.MOUSEBUTTONDOWN:
                cur = pos
            if event.type == pg.MOUSEBUTTONUP:
                right_triangle(screen, cur, pos, t, mycolour)
        elif d['triangle'] == True:
            if event.type == pg.MOUSEBUTTONDOWN:
                cur = pos
            if event.type == pg.MOUSEBUTTONUP:
                triangle(screen,[cur, pos,((pos[0] - cur[0])*cos(pi/3) - (pos[1] - cur[1])*sin(pi/3) + cur[0], (pos[0] - cur[0])*sin(pi/3) + (pos[1] - cur[1])*cos(pi/3) + cur[1])], t, mycolour)
        elif d['rhombus'] == True:
            if event.type == pg.MOUSEBUTTONDOWN:
                cur = pos
            if event.type == pg.MOUSEBUTTONUP:
                rhombus(screen, cur, pos, t, mycolour)
        elif d['eraser'] == True:
            if event.type == pg.MOUSEBUTTONDOWN:
                (x, y) = pos
                pg.draw.rect(screen, (255, 255, 255), (x, y, lastik_size, lastik_size))
                eraser = True
            if event.type == pg.MOUSEMOTION:
                if eraser:
                    pg.draw.rect(screen, (255, 255, 255), (pos[0], pos[1], lastik_size, lastik_size))
            if event.type == pg.MOUSEBUTTONUP:
                eraser = False

    pg.display.update()
pg.quit()