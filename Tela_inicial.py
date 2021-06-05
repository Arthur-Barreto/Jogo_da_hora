import pygame as pg
import random
from os import path
import Assets
from Config import IMG_DIR,FPS,BLACK

def start_screen(window):
    #Ajuste velocidade
    clock = pg.time.Clock()
    #Criando
    background = pg.image.load(path.join(IMG_DIR,"startsc_anim")).convert()
    background_rect = background.get_rect()

    running = True
    while running:
        #Set Velocidade Jogo
        clock.tick(FPS)
        #Processa Eventos
        for event in pg.event.get():
            #Verificar fechamento
            if event.type == pg.QUIT:
                state = QUIT
                running = False
            if event.type == pg.KEYUP:
                state = GAME
                running = False
        #A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background,background_rect)
        #Inverte o Display
        pg.display.flip()
    return state
