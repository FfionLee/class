import pygame

pygame.init()

screen=pygame.display.set_mode((600,600))

black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
white=(255,255,255)

playing=True

class Rectangles():
    def __init__(self,color,dimensions):
        self.c=color
        self.d=dimensions
        self.s=screen
    def draw(self):
        pygame.draw.rect(self.s,self.c,self.d)

rect1=Rectangles(blue,(10,10,50,100))
rect2=Rectangles(red,(100,100,200,100))
rect3=Rectangles(green,(400,200,100,200))



while playing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
    screen.fill(white)
    rect1.draw()
    rect2.draw()
    rect3.draw()
    pygame.display.update()


