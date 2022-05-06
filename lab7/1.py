import pygame as pg 
import math
from datetime import datetime
pg.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0 )
GREEN = (0,255,0)
BLUE = (0,0,255)

def rotation(surf, image, topleft, angle):

    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect.topleft)

screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Часики")


clock = pg.time.Clock()
font = pg.font.SysFont('Times New Roman', 25)
running = True

background = pg.image.load('images/micky1.jpg')
background = pg.transform.scale(background,(WIDTH, HEIGHT))


hand1 = pg.image.load('images/left4.png').convert_alpha()
hand2 = pg.image.load('images/hand5.png').convert_alpha()

#rect1 = hand1.get_rect() 


##cl = dict(zip(range(60), range(0, 360, 6)))

def time_to_angle(time):
    return 360 - time*6


angle = 0

while running:
    clock.tick(1)
 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.blit(background, (0, 0))

    t = datetime.now()
    vremya = font.render(f'{t:%H:%M:%S}', True, BLUE)
    screen.blit(vremya,(45, 75))
    angle = time_to_angle(t.second+1.5)
    angle2 = time_to_angle(t.minute)
    rotation(screen, hand1, (255,150), angle)
    rotation(screen, hand2, (255, 150), angle2)
    # angle -= 6


    
    pg.display.flip()
pg.quit()


