import math

import pygame as pg
from random import randint, random

from Tools.demo.spreadsheet import center

pg.init()
pg.display.set_caption("Бродилка")



WIDHT = 1090
HEIGHT = 738
screen = pg.display.set_mode((WIDHT, HEIGHT))
back_image = pg.image.load('kHPCvZKZasEtnzIAgJKzk4IvUCysTNGJmtGoxEEY3NlgnwUEg8xXvEs17w25SO4M7nhGftOYYxdlwiVbpPUqjE0A.jpg')
back_rect = back_image.get_rect() #карта
timer = pg.image.load('kHPCvZKZasEtnzIAgJKzk4IvUCysTNGJmtGoxEEY3NlgnwUEg8xXvEs17w25SO4M7nhGftOYYxdlwiVbpPUqjE0A.jpg')
timer = pg.transform.scale(timer,(100,100)) #это даже я не знаю что-чакое но надо

shet_kill =pg.image.load('unnamed.png')
shet_kill = pg.transform.scale(shet_kill,(100,100)) #Это тоже я не знаю что
char_image = pg.image.load('unnamed2.png')
char_image = pg.transform.scale(char_image, (100, 100)) #Персонаж
zombi = pg.image.load('unnamed.png')
zombi = pg.transform.scale(zombi,(150,150)) #Зомби
patron = pg.image.load('02f0285554bb7a6.png')
patron = pg.transform.scale(patron,(20,20)) #Патрон
patron2 = pg.image.load('02f0285554bb7a6 (1).png')
patron2 = pg.transform.scale(patron2,(20,20)) #Патрон для дробовика
patron3 = pg.image.load('02f0285554bb7a6 (2).png')
patron3 = pg.transform.scale(patron3,(20,20)) #Патрон для дробовика
char_image2 = pg.image.load('screen-1.png')
char_image2 = pg.transform.scale(char_image2, (100, 100))
char_rect = char_image.get_rect()
schet_kill_rect = shet_kill.get_rect(center=(855,690))
timer_rect = timer.get_rect(center=(2000,2000))
zombi_rect = zombi.get_rect(center=(400,300))
patron_rect = patron.get_rect(center=(100000,1))
patron_rect2 = patron2.get_rect(center=(100000,1))
patron_rect3 = patron3.get_rect(center=(100000,1))
left_image1 = char_image.copy()
right_image1 = pg.transform.flip(char_image.copy(), 1, 0)
down_image = pg.transform.flip(char_image.copy(), 0, 1)
up_image = pg.transform.flip(char_image.copy(), 0, 1)

right_image2 = pg.transform.flip(char_image2.copy(), 1, 0)
left_image2 = char_image2.copy()
left_image_zombi = pg.transform.flip(zombi.copy(), 0, 1)
ball_patron = 5 #кол-во патрон
ball_patron2 = 3
f1 = pg.font.SysFont('Arial Black', 50)
text = f1.render(str(0), True, (255, 255,255))
f2 = pg.font.SysFont('Jokerman', 50)
text2 = f2.render(str(0), True, (255, 0,50))
speed = 2
a = ball_patron
balls_gun = 0 #это надо но долго обьяснять
balls_dwizh = 0#это надо но долго обьяснять
zombi_hp = 0#это надо но долго обьяснять
balls_zomb = 0#это надо но долго обьяснять

right_image = right_image1
left_image = left_image1
def check_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
    return True

def check_move():
    global char_image
    global char_rect
    global map
    global zombi
    global zombi_rect
    global right_image
    global left_image
    global down_image
    global up_image
    global patron_rect
    global patron
    global balls_gun
    global balls_dwizh
    global ball_patron
    global text
    global f1
    global timer_rect
    global timer
    global zombi_hp
    global balls_zomb
    global text2
    global a
    global patron_rect2
    global patron_rect3
    keys = pg.key.get_pressed()

    f1 = pg.font.SysFont('Arial Black', 50)
    text = f1.render(str(a), True, (255, 255,255))

    f2 = pg.font.SysFont('Jokerman', 50)
    text2 = f2.render(str(balls_zomb), True, (96, 5, 4))
    if keys[pg.K_1]:
        char_image = pg.image.load('unnamed2.png')
        char_image = pg.transform.scale(char_image, (100, 100))
        right_image = right_image1
        left_image = left_image1
        balls_gun = 0
        a = ball_patron

    if keys[pg.K_w] and char_rect.top > 0:
        char_rect.y -= 2

    if keys[pg.K_s] and char_rect.bottom < HEIGHT:

        char_rect.y += 2
    if keys[pg.K_a] and char_rect.left > 0:
        char_image = right_image
        char_rect.move_ip((-speed, 0))
        balls_dwizh = 1
    if keys[pg.K_d] and char_rect.right < WIDHT:
        char_image = left_image
        char_rect.move_ip((speed, 0))

    if keys[pg.K_LSHIFT] and keys[pg.K_a] and char_rect.left > 0:
        char_image = right_image
        char_rect.move_ip((-3, 0))

    if keys[pg.K_LSHIFT] and keys[pg.K_d] and char_rect.right < WIDHT:
        char_image = left_image
        char_rect.move_ip((3, 0))

    if keys[pg.K_LSHIFT] and keys[pg.K_w] and char_rect.top > 0:
        char_image = left_image
        char_rect.y -= 3
    if keys[pg.K_LSHIFT] and keys[pg.K_s] and char_rect.bottom < HEIGHT:
        char_rect.y += 3

    if keys[pg.K_2]:
        balls_gun = 1
        char_image = char_image2
        right_image = right_image2
        left_image = left_image2
        a = ball_patron2

    mat = (math.sqrt((zombi_rect.x - char_rect.x) ** 2 + (zombi_rect.y - char_rect.y) ** 2))

    mat_kill = (math.sqrt((patron_rect.x - zombi_rect.x) ** 2 + (patron_rect.y - zombi_rect.y) ** 2))
    mat_kill2 = (math.sqrt((patron_rect2.x - zombi_rect.x) ** 2 + (patron_rect2.y - zombi_rect.y) ** 2))
    mat_kill3 = (math.sqrt((patron_rect3.x - zombi_rect.x) ** 2 + (patron_rect3.y - zombi_rect.y) ** 2))
    if char_image == right_image:
        balls_dwizh = 1
    if char_image == left_image:
        balls_dwizh = 0

    if zombi_rect.centerx < char_rect.centerx:
        zombi = left_image_zombi
        zombi_rect.move_ip(1,0)

    if zombi_rect.centery < char_rect.centery:

        zombi_rect.move_ip(0,1)

    if zombi_rect.centerx > char_rect.centerx:
        zombi = left_image_zombi
        zombi_rect.move_ip(-1,0)

    if zombi_rect.centery > char_rect.centery:

        zombi_rect.move_ip(0,-1)


    if ball_patron > 0:
        if balls_gun == 0 and keys[pg.K_f]:
            patron_rect = patron.get_rect(center=(char_rect.centerx - 1,char_rect.centery + 19))
            timer_rect.move_ip(10,0)
            if timer_rect.centerx == 2100:
                timer_rect = timer.get_rect(center=(2000,2000))
                ball_patron -= 1
        if balls_gun == 1 and keys[pg.K_f]:
            patron_rect = patron.get_rect(center=(char_rect.centerx - 1, char_rect.centery + 19))
            patron_rect2 = patron2.get_rect(center=(char_rect.centerx - 12, char_rect.centery + 19))
            patron_rect3 = patron3.get_rect(center=(char_rect.centerx - 1, char_rect.centery + 19))
            timer_rect.move_ip(10, 0)
            if timer_rect.centerx == 2100:
                timer_rect = timer.get_rect(center=(2000, 2000))
                ball_patron -= 1

    if patron_rect.centerx < 1090 or patron_rect.centerx > 0 :
        if patron_rect.centerx < 1090 and patron_rect.centerx > 0 and balls_dwizh == 0:
            patron_rect.move_ip((50, 0))
        if patron_rect.centerx < WIDHT and patron_rect.centerx > 0  and balls_dwizh == 1:
            patron_rect.move_ip(-50,0)
    if patron_rect2.centerx < 1090 or patron_rect2.centerx > 0 :
        if patron_rect2.centerx < 1090 and patron_rect2.centerx > 0 and balls_dwizh == 0:
            patron_rect2.move_ip((50, 25))
        if patron_rect2.centerx < WIDHT and patron_rect2.centerx > 0  and balls_dwizh == 1:
            patron_rect2.move_ip(-50,-75)
    if patron_rect3.centerx < 1090 or patron_rect3.centerx > 0 :
        if patron_rect3.centerx < 1090 and patron_rect3.centerx > 0 and balls_dwizh == 0:
            patron_rect3.move_ip((50, 75))
        if patron_rect3.centerx < WIDHT and patron_rect3.centerx > 0  and balls_dwizh == 1:
            patron_rect3.move_ip(-50,-25)
    if mat_kill < 100 or mat_kill2 < 100 or mat_kill3 < 100:
        zombi_hp +=1
        patron_rect = patron.get_rect(center=(1090, 20002))

    if zombi_hp == 3:
        zombi_rect =  zombi.get_rect(center=(4000,200))
        balls_zomb +=1
        zombi_hp = 0




def draw():
    screen.blit(back_image, back_rect)
    screen.blit(char_image, char_rect)
    screen.blit(zombi,zombi_rect)
    screen.blit(patron,patron_rect)
    screen.blit(patron2, patron_rect2)
    screen.blit(patron3, patron_rect3)
    screen.blit(text,(1000,650))
    screen.blit(timer,timer_rect)
    screen.blit(shet_kill,schet_kill_rect)
    screen.blit(text2,(900,650))
def update():
   check_move()
   pg.display.flip()
   pg.time.Clock().tick(165)

while check_events():
   draw()
   update()



pg.quit()