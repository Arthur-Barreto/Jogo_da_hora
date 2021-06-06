import pygame as pg
from Assets import *
from sprites import *
from Config import FASE1, QUIT

def start_screen(window):
    #Definindo variavel de Velocidade
    clock = pg.time.Clock()
    #Definindo Indice
    i=0
    #Definindo Frames por Segundo
    FPS_sc = 1
    #Definindo Estado do While
    start_screen = True
    #Sistema para criar animações
    while start_screen:
        #Setando Frames por segundo
        clock.tick(FPS_sc)
        #Alterando imagem
        window.blit(assets["startsc_anim"][i%2],(0,0))
        #Detectando eventos
        for event in pg.event.get():
            #Aperte Enter para começar / Quebrar Looping
            if event.type== pg.KEYDOWN: #Detecta Evento de Apertar
                if event.key == pg.K_RETURN:
                    state = FASE1
                    start_screen=False
            if event.type == pg.QUIT:
                state = QUIT
                start_screen = False
        pg.display.update()
        i+=1
    return state
    

