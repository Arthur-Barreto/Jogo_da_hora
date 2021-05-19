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

gif_tela_inical = pg.image.load("Tela Inicial/Gif Tela Inicial.gif").convert_alpha()
gif_tela_inical_big = pg.transform.scale(gif_tela_inical,(WIDTH,HEIGHT))

# == Start Screen ==
while start_screen:
    for event in pg.event.get():
        #Carregando imagem
        #Direcionando imagem
        window.blit(gif_tela_inical_big,(0,0))
        #Aperte Enter para começar / Quebrar Looping
        if event.type== pg.KEYDOWN: #Detecta Evento de Apertar
            if event.key == pg.K_RETURN:
                start_screen=False
        pg.display.update()
        if event.type == pg.QUIT:
            game = False
#Imagens
background = pg.image.load("")
# ===== Game Loop =====
while game:
    #Trata Eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
    #Saidas
    window.fill((255,255,255))
    window.bli
    #Update
    pg.display.update()

#===== Finalização =====
pg.quit()
