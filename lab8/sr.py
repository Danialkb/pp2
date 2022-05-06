import random
import pygame as pg
import time
import json

pg.init()

with open('high.json', 'r', encoding='utf8') as f:
    x = f.read()
n = 0
d = json.loads(x)
FPS = 60
WIDTH = 400
HEIGHT = 600
STEP = 5
ENEMTY_STEP = 7
lose = False
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCORE  = 0

clock =  pg.time.Clock()
coin = 0
rand_im = 0
lose_im = pg.image.load('images/lose.png')
score_font =  pg.font.SysFont("Verdana", 20)
coin_font =  pg.font.SysFont("Verdana", 20)
pg.mixer.music.load('sound/back.wav')
pg.mixer.music.play(-1)
SURF =  pg.display.set_mode((WIDTH, HEIGHT)) 
pg.display.set_caption("Street Racer")

bg =  pg.image.load("images/AnimatedStreet.png")

class Player (pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =  pg.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self): # перемещение игрока
        pressed_keys =  pg.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys [pg.K_a]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < WIDTH:
            if pressed_keys [pg.K_d]:
                self.rect.move_ip(STEP, 0)

        if self.rect.top > 0:
            if pressed_keys [pg.K_w]:
                self.rect.move_ip(0, -STEP)

        if self.rect.bottom < HEIGHT:
            if pressed_keys [pg.K_s]:
                self.rect.move_ip(0, STEP)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pg.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        global rand_im
        self.rand_num = random.randint(0, 2)
        rand_im = self.rand_num
        self.im = pg.image.load(f'images/coin{self.rand_num}.png') # появление рандомных картинок с разными размерами
        self.rect = self.im.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

    def draw(self):
        SURF.blit(self.im, self.rect)

class Enemy (pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =  pg.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def update(self):
        global SCORE
        self.rect.move_ip(0, ENEMTY_STEP)
        if(self.rect.bottom > HEIGHT): # если вражеская машина прошла дорогу то увеличиваем score и возвращаем машину обратно
            SCORE += 1
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)



P1 = Player()
E1 = Enemy()
C1 = Coin()
y = 0
check = True
enemies =  pg.sprite.Group()
enemies.add(E1)

monetki = pg.sprite.Group()
monetki.add(C1)
while True:
    clock.tick(FPS)
    for event in  pg.event.get():
        if event.type ==  pg.QUIT:
            pg.quit()


    P1.update()
    E1.update()

    if  pg.sprite.spritecollideany(P1, enemies):
        pg.mixer.Sound('sound/crash.wav').play() # играется звук столкновения игрока и вражеской машины
        time.sleep(0.8)
        if d['highscore_for_streetracer'] < coin:
            d['highscore_for_streetracer'] = coin
            with open('high.json', 'w', encoding='utf8') as f:
                f.write(json.dumps(d, indent=4))
                # запись наилучшего результата
        lose = True # активация окна проигрыша
   

    SURF.blit(pg.transform.scale(bg, (WIDTH, HEIGHT)), (0, y % HEIGHT))
    SURF.blit(pg.transform.scale(bg, (WIDTH, HEIGHT)), (0, -HEIGHT + (y % HEIGHT))) # движущаяся дорога

    y += 2
    for monetka in monetki:
        monetka.draw()
        if pg.sprite.collide_rect(P1, monetka): # коллизия игрока и монетки
            monetka.kill() 
            if rand_im == 0:    # score увеличивается на 1 для картинки с номером 0
                coin += 1
                n += 1
            elif rand_im == 1: # score увеличивается на 5 для картинки с номером 1
                coin += 5
                n += 1
            elif rand_im == 2:  # score увеличивается на 10 для картинки с номером 2
                coin += 10
                n += 1

            newC = Coin()
            monetki.add(newC) # старая монетка "умирает" -----> в рандомном месте появляется новая
    E1.draw(SURF)
    P1.draw(SURF)

    score_img = score_font.render(str(SCORE), True, BLACK)
    coin_collected = coin_font.render(f'{coin}', True, BLACK)
    SURF.blit(score_img, (10, 10)) # текущий счет
    SURF.blit(coin_collected, (350, 10)) # количество очков с собранных монет
    if n  ==  10 and check: # при получении n-й монеты увеличиваем скорость вражеской машины
        ENEMTY_STEP += 5
        check = False
    while lose: # окно проигрыша
        pg.mixer.music.stop()
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        SURF.fill(BLACK)
        SURF.blit(lose_im, (0, 60))
        
        pg.display.flip()

    pg.display.update()


