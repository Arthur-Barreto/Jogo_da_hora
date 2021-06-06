import pygame as pg
from Config import *
from Assets import *
from sprites import *

def death_screen(window):
    #Variavle para o ajuste de velocidade
    clock = pg.time.Clock()
    i=0
    LOADING = 5
    window = pg.display.set_mode((800, 800))
    while morte:
        clock.tick(LOADING)
        window.blit(assets["loading"][i%2],(0,0))
        for event in pg.event.get():
            #Aperte Enter para começar / Quebrar Looping
            if event.type== pg.KEYDOWN: #Detecta Evento de Apertar
                if event.key == pg.K_RETURN:
                    morte=False
            if event.type == pg.QUIT:
                morte = False
        pg.display.update()
        i+=1
        if i > 100:
            morte = False