# ===== Inicialização =====
#Import
import pygame as pg
import random
import time
from Tela_inicial import start_screen
from settings import *
from Assets import*

pg.init()
# Inicializa o pygame, as configurações e o objeto screen
ms_settings = Settings()    
# menu
menu = pg.display.set_mode((ms_settings.menu_width, ms_settings.menu_height))
pg.display.set_caption("Metal Slug Remake")
assets=load_assets()
#-----Estrutura de dados
game = True
start_screen = True
FPS_sc=1
FPS=30
#Variavel para Ajuste de velocidade
clock = pg.time.Clock()
gif_tela_inical = pg.image.load("Tela Inicial/Gif Tela Inicial.gif").convert_alpha()
gif_tela_inical_big = pg.transform.scale(gif_tela_inical,(ms_settings.menu_width, ms_settings.menu_height))


# == Start Screen ==
i=0
while start_screen:
    clock.tick(FPS_sc)
    menu.blit(assets["startsc_anim"][i%2],(0,0))
    for event in pg.event.get():
        #Aperte Enter para começar / Quebrar Looping
        if event.type== pg.KEYDOWN: #Detecta Evento de Apertar
            if event.key == pg.K_RETURN:
                start_screen=False
        if event.type == pg.QUIT:
            start_screen = False
    pg.display.update()
    i+=1
#Tela principal
window = pg.display.set_mode((ms_settings.screen_width, ms_settings.screen_height))
pg.display.set_caption("Metal Slug Remake Bom Jogo")
# ===== Game Loop =====
i = 0
while game:
    #Trata Eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
    #Saidas
    window.fill(ms_settings.bg_color)
    window.blit(assets["player"][i%2],(300,200))
    #Update
    pg.display.update()
    i += 1
#===== Finalização =====
pg.quit()