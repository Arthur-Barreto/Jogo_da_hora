import pygame as pg
import os
Start_screen = "startsc_anim"

#Variaveis
HEIGHT_P= 38
WIDTH_P= 29

def load_assets():
    #Definindo Assets
    assets={}
    #Animação Tela Inicial
    start_sc=[]
    start_sc.append(pg.image.load("Tela Inicial/TIS0.png").convert())
    start_sc.append(pg.image.load("Tela Inicial/TIS1.png").convert())
    assets["startsc_anim"] = start_sc
    #Animação Jogador - Andando Frente
    PF_Anim = []
    for e in range(0,23):
        nome_arquiva = "Jogador/PlayerWalking/{}.png".format[e]
        img = pg.image.load(nome_arquiva).convert()
        img = pg.transform.scale(img,(HEIGHT_P,WIDTH_P))
        PF_Anim.append(img)
    assets["player"] = PF_Anim
    #Animação Jogador - Andando trás
    #Animação Jogador - Pulando
    print (assets["startsc_anim"])
    return assets