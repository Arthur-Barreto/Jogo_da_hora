import pygame as pg
import os
Start_screen = "startsc_anim"

def load_assets():
    #Definindo Assets
    assets={}
    #Animação Tela Inicial
    start_sc=[]
    start_sc.append(pg.image.load("Tela Inicial/TIS0.png").convert())
    start_sc.append(pg.image.load("Tela Inicial/TIS1.png").convert())
    assets["startsc_anim"] = start_sc
    #Animação Jogador - Andando Frente
    
    #Animação Jogador - Andando trás
    #Animação Jogador - Pulando
    print (assets["startsc_anim"])
    return assets