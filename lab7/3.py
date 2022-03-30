import pygame as pg

pg.init()
w, h = 800, 600
clock = pg.time.Clock()
fps = 30
white = (255, 255, 255)
ball = (0, 51, 65)
x, y = w//2, h//2
dx, dy = 0, 0

speed = 20
screen = pg.display.set_mode((w,h))
is_running = True

while is_running:
    clock.tick(fps)

    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            is_running = False
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_RIGHT:
                dy = 0
                dx = speed
                
            if ev.key == pg.K_LEFT:
                dy = 0
                dx = -speed
            if ev.key == pg.K_UP:
                dx = 0
                dy = -speed
            if ev.key == pg.K_DOWN:
                dx = 0
                dy = speed
            
    screen.fill(white)

    pg.draw.circle(screen, pg.Color('forestgreen'), (x%w,y%h), 25)

    x += dx
    y += dy

    pg.display.flip()

pg.quit()