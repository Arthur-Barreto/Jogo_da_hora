# ===== Inicialização =====
#Import
import pygame as pg
import random
import time
from Tela_inicial import start_screen
from settings import *

pg.init()
# Inicializa o pygame, as configurações e o objeto screen
ms_settings = Settings()    
#Tela principal
window = pg.display.set_mode((ms_settings.screen_width, ms_settings.screen_height))
# menu
menu = pg.display.set_mode((ms_settings.menu_width, ms_settings.menu_height))
pg.display.set_caption("Metal Slug Remake")

#-----Estrutura de dados
game = True
start_screen = True
FPS_sc=1
FPS=30
#Variavel para Ajuste de velocidade
clock = pg.time.Clock()
gif_tela_inical = pg.image.load("Tela Inicial/Gif Tela Inicial.gif").convert_alpha()
gif_tela_inical_big = pg.transform.scale(gif_tela_inical,(ms_settings.menu_width, ms_settings.menu_height))
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
            # aqui para sair com o x tem que ser start_screen
            # no lugar de game, agr da ok
            start_screen = False
    pg.display.update()
    i+=1

# ===== Game Loop =====
while game:
    print("entrei no loop do jogo")
    #Trata Eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print("estou saindo do jogo")
            game = False
    #Saidas
    window.fill(ms_settings.bg_color)
    #Update
    pg.display.update()

#===== Finalização =====
pg.quit()
