# ===== Inicialização =====
#Import
import pygame as pg
import random
import time
from Tela_inicial import start_screen

#Init
pg.init()

#Tela principal
WIDTH = 800
HEIGHT = 800
window = pg.display.set_mode ((WIDTH,HEIGHT))
pg.display.set_caption("Metal Slug Remake")

#-----Estrutura de dados
game = True
start_screen = True
FPS_sc=1
FPS=30
#Variavel para Ajuste de velocidade
clock = pg.time.Clock()
gif_tela_inical = pg.image.load("Tela Inicial/Gif Tela Inicial.gif").convert_alpha()
gif_tela_inical_big = pg.transform.scale(gif_tela_inical,(WIDTH,HEIGHT))
start_sc=[]
start_sc.append(pg.image.load("Tela Inicial/TIS0.png").convert())
start_sc.append(pg.image.load("Tela Inicial/TIS1.png").convert())

# == Start Screen ==
i=0
while start_screen:
    clock.tick(FPS_sc)
    window.blit(start_sc[i%2],(0,0))
    for event in pg.event.get():
        #Aperte Enter para começar / Quebrar Looping
        if event.type== pg.KEYDOWN: #Detecta Evento de Apertar
            if event.key == pg.K_RETURN:
                start_screen=False
        if event.type == pg.QUIT:
            game = False
    pg.display.update()
    i+=1

# ===== Game Loop =====
while game:
    #Trata Eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
    #Saidas
    window.fill((255,255,255))
    #Update
    pg.display.update()

#===== Finalização =====
pg.quit()
