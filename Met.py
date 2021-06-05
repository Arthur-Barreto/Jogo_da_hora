#Importando Pygame
import pygame as pg
pg.init()
window = pg.display.set_mode((800,800))
pg.display.set_caption("Hello World")

game = True

font = pg.font.SysFont(None, 48)
text = font.render("HELLO WORLD", True, (0,0,255))

while game:
    for event in pg.event.get():
        #------Verifica consequências
        if event.type == pg.QUIT:
            game = False
        
        #Gera Saídas
    window.fill((255,255,255))
    window.blit(text,(10,10))
    pg.display.update()
pg.quit()