#===== Inicialização =====
#Importa e inicia bibliotecas/Pacotes
import pygame as pg
from Config import *

pg.init()
pg.mixer.init()
window = pg.display.set_mode((800,800))
pg.display.set_caption("Metal Slug")
from Assets import font
from Tela_inicial import start_screen
from Game_Screen import fase1,fase2,loading,death_screen
lifes = 2
indice = 2
#Gera Tela Entrada
state = INIT
while state != QUIT:
    if state == INIT:
        state = start_screen(window)
    elif state == "FASE1":
        state = fase1(window,lifes)
        if state == LOAD:
            state = loading(window,indice)
        elif state == DEATH:
            state = death_screen(window)
    elif state == "FASE2":
        state = fase2(window,lifes)
        if state == LOAD:
            state = loading(window,indice)
        elif state == DEATH:
            state = death_screen(window)
    else:
        state = QUIT
    
#===== Finalização =====
pg.quit()