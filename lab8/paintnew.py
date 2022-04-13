import pygame as  pg

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (122, 239, 173)
BROWN = (102, 51, 0)
BLACK = (0, 0, 0)
BACKGROUND = (255, 255, 255)

pg.init()
screen = pg.display.set_mode((800, 600))

surf = pg.Surface((700, 600))
buttons = pg.Surface((100, 600))

commands = {
    'rect': [52, 4, 44, 44],
    'circle': [4,50, 44, 44],
    'eraser': [52, 50, 44, 44]
}

def set_surf():
    surf.fill(BACKGROUND)
    
    buttons.fill(WHITE)
    pg.draw.rect(buttons, BLACK, (2, 2, 96, 596), 1)
    
    for i in commands:
        pg.draw.rect(buttons, BLACK, commands[i], 1)
    
    pg.draw.rect(buttons, BLACK, (58, 10, 32, 32), 1)
    pg.draw.circle(buttons, BLACK, (27, 70), 15, 1)

    pg.draw.rect(buttons, BACKGROUND, (56, 58, 36, 28))
    
    
    screen.blit(surf, (0, 0))
    screen.blit(buttons, (700, 0))
        

def rectangle(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1-x2)
    height = abs(y1-y2)

    if x1 <= x2:
        if y1 < y2:
            pg.draw.rect(screen, color, (x1, y1, width, height), d)
        else:
            pg.draw.rect(screen, color, (x1, y2, width, height), d)
    else:
        if y1 < y2:
            pg.draw.rect(screen, color, (x2, y1, width, height), d)
        else:
            pg.draw.rect(screen, color, (x2, y2, width, height), d)



def circle(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1-x2)
    height = abs(y1-y2)

    if x1 <= x2:
        if y1 < y2:
            pg.draw.ellipse(screen, color, (x1, y1, width, height), d)
        else:
            pg.draw.ellipse(screen, color, (x1, y2, width, height), d)
    else:
        if y1 < y2:
            pg.draw.ellipse(screen, color, (x2, y1, width, height), d)
        else:
            pg.draw.ellipse(screen, color, (x2, y2, width, height), d)


last_pos = (0, 0)
w = 2
draw_line = False
erase = False
ed = 50

d = {
    'rect': False,
    'circle': False,
    'eraser': False
}

set_surf()
running = True
score = 0
while running:
    pos = pg.mouse.get_pos()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pg.image.save(surf, f'./image_{score}.jpg')
                score += 1
            
        if event.type == pg.MOUSEBUTTONDOWN:
            for k, v in commands.items():
                if v[0] <= pos[0]-700 <= v[0] + v[2] and v[1] <= pos[1] <= v[1] + v[3]:
                    d[k] = True
                    for i, j in d.items():
                        if i != k:
                            d[i] = False
                    break

        if d['rect'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                rectangle(surf, last_pos, pos, w, (255, 0, 0))
        elif d['circle'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pg.MOUSEBUTTONUP:
                # rectangle(screen, last_pos, pos, d, (255, 0, 0))
                circle(surf, last_pos, pos, w, (255, 0, 0))
        elif d['eraser'] == 1:
            if event.type == pg.MOUSEBUTTONDOWN:
                (x, y) = pos
                pg.draw.rect(surf, BACKGROUND, (x, y, ed, ed))
                erase = True
            if event.type == pg.MOUSEMOTION:
                if erase:
                    pg.draw.rect(surf, BACKGROUND, (pos[0], pos[1], ed, ed))
            if event.type == pg.MOUSEBUTTONUP:
                erase = False
    
    
    
    for k, v in d.items():
        if v == True:
            pg.draw.rect(buttons, RED, commands[k], 1)
        else:
            pg.draw.rect(buttons, BLACK, commands[k], 1)
            
    
    screen.blit(buttons, (700, 0))
    screen.blit(surf, (0, 0))
    
        

    pg.display.update()
pg.quit()