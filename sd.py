import pygame
from time import *
from data import *
import webbrowser
pygame.init()
pygame.display.set_caption('Escape from Almaty')

#zastavka=input('хотите посмотреть заставку?(да/нет)')
#if zastavka=='да':
#    webbrowser.open('https://www.youtube.com/watch?v=AqM-N4h3ViI')

class Chvk():
    def __init__(self,png,x,y,width,heigth,hp):
        self.rect=pygame.Rect(x, y, width, heigth)
        self.png=pygame.image.load(png)
        self.hp=hp
    def drawd(self):
        linox.blit(self.png,(self.rect.x,self.rect.y))
    def fill(self):
        pygame.draw.rect(linox,self.fire)
    def update(self,key_p):
        if key_p[pygame.K_a]and pl.rect.x>0:
            self.rect.x-=2
        if key_p[pygame.K_d]and pl.rect.y+50<500:
            self.rect.x+=2

class Pl(Chvk):
    def __init__(self,png,x,y,width,heigth,hp):
        super().__init__(png,x,y,width,heigth,hp)
    def bullet_1(self):
        global bull,bung,bullett,bang
        if bull<=1000 and bull>0:
            bullett.fire_2.x-=5
            bullett.draw_fire_2()
            bull-=1
        if bung<=1000 and bung>0:
            bang.bangg()
            bung-=1
class En(Chvk):
    def __init__(self,png,x,y,width,heigth,hp):
        super().__init__(png,x,y,width,heigth,hp)
    def bullet_2(self):
        global en_bull,en_bung,en_bullett,en_bang
        if en_bull<=1000 and en_bull>0:
            en_bullett.fire_2.x+=3
            en_bullett.draw_fire_2()
            en_bull-=1
        if en_bung<=1000 and en_bung>0:
            en_bang.bangg()
            en_bung-=1
#'w-прыжок d-идти в право a-идти в лево',30)

temp_str=70
f_x=250
f_y=250
kill=0
kill2=0
x=0
y=0
temp=0
points=0
bull=0
wall_down_time=0
wall_up_time=0
bullets=8
bullets_mag=6
anim=False
bung=0

nadpis=Card(250,5,0,0)
nadpis.set_text(0,30)
score=Card(200,5,0,0)
score.set_text('Счёт:',30)
bullets_score=Card(200,25,0,0)
bullets_score.set_text('Патроны:',30)
bullets_score2=Card(280,25,0,0)
bullets_score2.set_text(bullets,30)
bullets_magz=Card(300,25,0,0)
bullets_magz.set_text('Магазины:',30)
bullets_magz2=Card(390,25,0,0)
bullets_magz2.set_text(bullets_mag,30)
finish=Card(180,150,0,0)

bg=pygame.image.load('bgg.png')
pl=Pl('pl2.png',275,192,46,78,100)
en=En('en2.png',100,192,49,78,100)
wall=Chvk('wall.png',200,-400,50,400,100)

#bullett=0 30 33

bullett=Bullet('bullet.png',50,600,600,25,10)
bang=Bang('bang!.png',600,600)
en_bullett=Bullet('bullett.png',25,600,600,25,10)
en_bang=Bang('bang!2.png',600,600)
en_bull=0
en_bung=0

linox=pygame.display.set_mode((500,400))
clock=pygame.time.Clock()
run=True

HP=Card(45,5,0,0)
HP.set_text('HP:',30)
HP_num_en=Card(75,5,0,0)
HP_num_en.set_text(en.hp,30)

HP2=Card(415,5,0,0)
HP2.set_text('HP:',30)
HP_num_pl=Card(445,5,0,0)
HP_num_pl.set_text(pl.hp,30)

bullets_book=[]
key_p=pygame.key.get_pressed()
#linox.fill((41, 227, 184))
#font=pygame.font.Font(None,30).render('TrueProger_and_FalseProger',True,(227, 68, 248 ))
while run:
    pygame.display.update()
    clock.tick(60)
    key_p=pygame.key.get_pressed()

    if bullets<=0 and bullets_mag>0:
        bullets+=8
        bullets_mag-=1

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and bullets>0:# and bullett.fir==0:
            bullett=Bullet('bullet.png',25,pl.rect.x-48,pl.rect.y-5,25,10)
            bullett.draw_fire()
            bullett.draw_fire_2()
            bang=Bang('bang!.png',pl.rect.x-65,pl.rect.y-11)
            bullett.bull=190
            bung=80
            bullets-=1
            bullets_book.append(bullett)
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w and pl.rect.y==192:
                pl.rect.y-=60
                temp=60
                
    pl.update(key_p)
    
    linox.blit(bg,(0,0))
    pl.drawd()
    en.drawd()
    wall.drawd()
    
    for bullett in bullets_book:
        if bullett.bull>0:
            bullett.fire_2.x-=5
            bullett.draw_fire_2()
            bullett.bull-=1
        if bullett.fire_2.x<=en.rect.x and bullett.fire_2.x>=en.rect.x-49 and bullett.fire_2.y>=en.rect.y-31 and bullett.fire_2.y<=en.rect.y+60 and anim==False:
            en.hp-=bullett.damage
            bullett.fire_2.x=5000
            if en.hp<=0:
                en.rect.x-=172
                kill=172
                anim=True
        if bullett.bull<=0:
            bullett.fire_2.x=5000
            bullets_book.remove(bullett)

    if pl.rect.y<=162 and temp<=0:
        pl.rect.y=192
    if temp<=160:
        temp-=1

    pl.bullet_1()
    #if bull<=1000 and bull>0:
    #    bullett.fire_2.x-=5
    #    bullett.draw_fire_2()
    #    bull-=1
    #if bung<=1000 and bung>0:
    #    bang.bangg()
    #    bung-=1
        
    if temp_str>0:
        temp_str-=1
    if temp_str<=0:
        en_bullet=Bullet('bullett.png',25,en.rect.x,en.rect.y+25,25,10)
        en_bang=Bang('bang!2.png',en.rect.x+11,en.rect.y-11)
        en_bullett.fire_2.x=en.rect.x+11
        en_bullett.fire_2.y=en.rect.y+28
        en_bullett.draw_fire_2()
        en_bung=80
        en_bull=150
        temp_str=150
    en.bullet_2()
    if en_bullett.fire_2.x<=pl.rect.x+48 and en_bullett.fire_2.x>=pl.rect.x-25 and en_bullett.fire_2.y<=pl.rect.y+77 and en_bullett.fire_2.y>=pl.rect.y:
            pl.hp-=en_bullett.damage
            en_bullett.fire_2.x=5000
            if pl.hp<=0:
                finish.set_text('Game over!',60)
                finish.draw_text()
                pygame.display.update()
                break

    if bullett.fire_2.x<=wall.rect.x and bullett.fire_2.x>=wall.rect.x-49 and bullett.fire_2.y>=wall.rect.y-200 and bullett.fire_2.y<=wall.rect.y+400:
        bullett.fire_2.x=5000

    HP.set_text('HP:',30)
    HP.draw_text()
    HP2.set_text('HP:',30)
    HP2.draw_text()

    HP_num_en.set_text(en.hp,30)
    HP_num_en.draw_text()
    HP_num_pl.set_text(pl.hp,30)
    HP_num_pl.draw_text()

    score.set_text('Счёт:',30)
    score.draw_text()
    nadpis.set_text(points,30)
    nadpis.draw_text()
    bullets_score.set_text('Патроны:',30)
    bullets_score.draw_text()
    bullets_score2.set_text(bullets,30)
    bullets_score2.draw_text()
    bullets_magz.set_text('Магазины:',30)
    bullets_magz.draw_text()
    bullets_magz2.set_text(bullets_mag,30)
    bullets_magz2.draw_text()

    if wall_down_time<=1000 and wall_down_time>0 and anim==True:
        wall.rect.y+=1
        wall_down_time-=1

    if wall_down_time<=1000 and wall_down_time>0 and anim==False:
        wall.rect.y=0
        wall_down_time-=1

    if wall_down_time==0:
        wall.rect.y=-400

    if kill==0:
        anim=False
    if en.hp<=0 and anim==False:
        en.hp=100
        points+=1
    
    if kill<=1000 and kill>0 and en.hp<=0 and anim==True:
        en.rect.x+=1
        kill-=1
    if points==10:
        linox.blit(bg,(0,0))
        score.set_text('Счёт:',30)
        score.draw_text()
        nadpis.set_text(points,30)
        nadpis.draw_text()
        finish.set_text('WIN',60)
        finish.draw_text()
        pygame.display.update()
        print('WIN!')
        run=False
        pygame.quit()
        break
