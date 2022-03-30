import pygame as pg

pg.init()
is_running = True,
WIDTH, HEIGHT = 800, 800
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
play = True
bg = pg.image.load('images/muspl.jpg')
mus = ['music/Astronaut.mp3', 'music/chistyi.mp3', 'music/mister718.mp3', 'music/Rampampam.mp3', 'music/Run.mp3']
current = 0
pg.mixer.music.load(mus[current])
pg.mixer.music.play()
# font = pg.font.SysFont('Times New Roman', 20, True)
while is_running:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                pg.mixer.music.pause() #press 'r' to pause

            if event.key == pg.K_p:
                pg.mixer.music.unpause() #press 'p' to unpause
            
            if event.key == pg.K_s:
                pg.mixer.music.stop() #press 's' to stop

            if event.key == pg.K_RIGHT:
                current += 1
                pg.mixer.music.load(mus[current]) #press '->' to play next song
                pg.mixer.music.play()
            if event.key == pg.K_LEFT:
                current -= 1
                pg.mixer.music.load(mus[current]) #press '<-' to play previous song
                pg.mixer.music.play()

    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    pg.display.flip()

pg.quit()
