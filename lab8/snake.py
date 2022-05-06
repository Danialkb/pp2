import pygame as pg
from random import randint, randrange
import time
import json
import psycopg2

username = input()
config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Dankb2131193*'
)

current = config.cursor()

sql = '''
    SELECT * FROM snakeusers WHERE username = %s;
'''
current.execute(sql, [username])
data = current.fetchone()

if data == None:
    sql = '''
        INSERT INTO snakeusers VALUES(%s, 0, 0);
    '''
    current.execute(sql, [username])
    config.commit()
else: 
    print(data)
pg.init()

lose = False
WIDTH, HEIGHT = 800, 800
FPS = 7
cell = 40 
image = pg.image.load('images/backforsnake.jpg')
font_score = pg.font.SysFont('Times New Roman', 30, True, True)
collided = False
rand_apple = 0

pg.mixer.music.load('sound/mus1.mp3')
TIMER = 5000
pg.mixer.music.load('sound/mus.mp3')
pg.mixer.music.play(-1)
levelcnt = pg.font.SysFont('Times New Roman', 30, True, True)
current_lev = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WALLCOLOR = (127, 72, 41)
surf = pg.Surface(400, 400)
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('ZHYLAN')
lose_im = pg.image.load('images/lose.png')
running = True

clock = pg.time.Clock()

class Food:
    def __init__(self):
        global rand_apple
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)
        self.rand = randint(0, 2)
        rand_apple = self.rand
        # self.r = 20
        self.im = pg.image.load(f'images/apple{self.rand}.png')

    def draw(self):

        screen.blit(self.im, (self.x, self.y)) # отображаю картинки моей еды


    def redraw(self): # функция перерисовки(чтобы еда не появлялась на стенах или на змейке)
        global rand_apple
        self.rand = randint(0, 2)
        self.im = pg.image.load(f'images/apple{self.rand}.png')
        rand_apple = self.rand
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)

class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.im1 = pg.image.load('images/stena.png')
        # self.im2 = pg.image.load('images/dari.jpg')

    def draw(self):
        screen.blit(self.im1, (self.x, self.y))
        

class Snake:
    def __init__(self):
        self.speed = cell
        self.body = [[80, 80]]
        self.dx = self.speed
        self.dy = 0
        self.direction = ''
        self.color = (207, 0, 15)
    
    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                # меняю направление моей змейки с помощью 'wasd' также прописал условию чтобы змейка не могла двигаться назад
                if event.key == pg.K_a and self.direction != 'right':
                    self.dx = -self.speed
                    self.dy = 0
                    self.direction = 'left'
                if event.key == pg.K_d and self.direction != 'left':
                    self.dx = self.speed
                    self.dy = 0
                    self.direction = 'right'
                if event.key == pg.K_w and self.direction != 'down':
                    self.dx = 0
                    self.dy = -self.speed
                    self.direction = 'up'
                if event.key == pg.K_s and self.direction != 'up':
                    self.dx = 0
                    self.dy = self.speed
                    self.direction = 'down'

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

        self.body[0][0] %= WIDTH  # проход через границы
        self.body[0][1] %= HEIGHT


    def draw(self): 
        pg.draw.rect(screen, self.color, (self.body[0][0], self.body[0][1], cell, cell)) # рисую голову отдельно чтобы она имела другой цвет

        for block in self.body[1:]: # рисую остальную часть тела
            pg.draw.rect(screen, (0, 187, 51), (block[0], block[1], cell, cell))
    
    def collision_food(self, f:Food): 
        if self.body[0][0] == f.x and self.body[0][1] == f.y: # коллизию с яблоком
            global score, collided
            if rand_apple == 0:
                score += 10
            elif rand_apple == 1:        # увеличиваем счет в зависимости от того какое яблоко съела змейка
                score += 20
            elif rand_apple == 2:
                score += 30
            self.body.append([1000, 1000])
            collided = True

    def collision_self(self):
        global running, lose
        if self.body[0] in self.body[1:]: # проигрыш если он сталкивается сам с собой
            # running = False 
            lose = True

    def eat_food(self, f:Food):
        if [f.x, f.y] in self.body: # если яблоко появляется на змейке перерисовываю ее
            f.redraw()


def wash():
    pg.time.set_timer(pg.USEREVENT, TIMER) # таймер для исчезания еды
S1 = Snake()
F1 = Food()
pause = False
score = 0
highscore = 0
level = 1

wash()


while not lose:
    clock.tick(FPS)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            lose = True
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pause = True 
        if event.type == pg.USEREVENT:
            F1.redraw() # 5 секунд прошло еда исчезла
        
        
    screen.blit(pg.transform.scale(image, (800,800)), (0, 0))
    
    walls_file = open(f'wall{level-1}.txt', 'r').readlines() # открываю файл с паттерном текущего уровня


    walls = []

    for i, line in enumerate(walls_file):
        for j, each in enumerate(line):
            if each == "#":
                walls.append(Wall(j * cell, i * cell)) # рисовка стен с помощью паттернов записанных в txt файлах

    if score >= 150 and score < 350:  # переходы на следующие уровни      
        level = 2                      
        FPS = 7                    
        FPS = 10
        current_lev = 2

    if score >= 350:
        level = 3
        current_lev = 3
        FPS = 12   
    F1.draw()
    S1.draw()
    S1.move(events)
    S1.collision_food(F1)
    S1.collision_self()
    S1.eat_food(F1)


    if collided == True:
        TIMER = 5000
        wash()
        collided = False
    for wall in walls:
        wall.draw()
        if F1.x == wall.x and F1.y == wall.y: # если еда появляется на стенах переисовываю ее
            F1.redraw()
        if S1.body[0][0] == wall.x and S1.body[0][1] == wall.y: # коллизия со стенками
            lose = True
            # running = False
            

    textscore = font_score.render(f'{score}', True, BLACK)
    textlvl = levelcnt.render(f'{current_lev}', True, BLACK)
    screen.blit(textscore, (10, 10)) # отображаю текущий счет
    screen.blit(textlvl, (780, 10)) # отображаю текущий уровень
    while paused: 
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
                paused = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_u:
                    paused = False # возобнавляем игру
                if event.key == pg.K_c:
                    a = score# обновляем текущие данные в базе данных
                    sql = '''
                        UPDATE users SET score = %s, level = %s WHERE username = %s;
                    '''
                    current.execute(sql, [a, level, username])
                    config.commit()
        screen.blit(surf, (200, 200))
        cntr = score.render(f'Your score is {score}', True, 'white')
        screen.blit(cntr, (315, 350))
        l = score.render(f'Your level is {level}', True, 'white')
        screen.blit(l, (317, 385))
        txt = score.render(f'Press "C" to save your current state', True, 'white')
        screen.blit(txt, (212, 420))
        pg.display.flip()
    pg.display.flip()
    
sql = '''
    UPDATE snakeusers SET score = %s, level = %s WHERE username = %s;
'''
current.execute(sql, [score, level, username])
config.commit()
current.close()
config.close()
pg.quit()