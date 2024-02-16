import pygame
linox=pygame.display.set_mode((500,400))
class Chvk():
    def __init__(self,png,x,y,width,heigth,hp):
        self.rect=pygame.Rect(x, y, width, heigth)
        self.png=pygame.image.load(png)
        self.hp=hp
    def drawd(self):
        linox.blit(self.png,(self.rect.x,self.rect.y))
    def fill(self):
        pygame.draw.rect(linox,self.fire)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

class Bullet():
    def __init__(self,bul,damage,x_b, y_b, width_b, heigth_b):
        self.bal=pygame.image.load(bul)
        self.damage=damage
        self.fire_2=pygame.Rect(x_b, y_b+10, width_b, heigth_b)
        self.coor_x=x_b
        self.coor_y=y_b
    def draw_fire(self):
        linox.blit(self.bal,(self.coor_x,self.coor_y))
    def draw_fire_2(self):
        linox.blit(self.bal,(self.fire_2.x,self.fire_2.y))
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

class Bang():
    def __init__(self,bang,x,y):
        self.bang=pygame.image.load(bang)
        self.x=x
        self.y=y
    def bangg(self):
        linox.blit(self.bang,(self.x,self.y))

class Card():#создание класса
    def __init__(self,x,y,width,heigth):
        self.rect=pygame.Rect(x, y, width, heigth)#создание прямоугольника    def set_text(self,text,fsize=40):
    def set_text(self,text,size):
        self.image=pygame.font.Font(None,size).render(str(text),True,(255,0,0))
    def draw_text(self):
        linox.blit(self.image,(self.rect.x,self.rect.y))
