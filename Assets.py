import pygame as pg
import os
Start_screen = "startsc_anim"

#Variaveis
HEIGHT_P= 52
WIDTH_P= 40

def load_assets():
    #Definindo Assets
    assets={}
    #====Telas====
    #StartScreen
    start_sc=[]
    start_sc.append(pg.image.load("Tela Inicial/TIS0.png").convert())
    start_sc.append(pg.image.load("Tela Inicial/TIS1.png").convert())
    assets["startsc_anim"] = start_sc
    #Game Background
    background=pg.image.load("Cenario/Montanha Clean 1100X300.png").convert()
    assets["background"] = background
    #====Jogador====
    #Idle
    PI_Anim = []
    for e in range(0,11):
        nome_arquiva = "Jogador/PlayerIdle/{}.png".format(e)
        img = pg.image.load(nome_arquiva).convert_alpha()
        img = pg.transform.scale(img,(WIDTH_P,HEIGHT_P))
        PI_Anim.append(img)
    assets["player"] = PI_Anim
    #Andando Frente
    PF_Anim = []
    for f in range (0,23):
        nome_arquivo = "Jogador/PlayerWalking/{}.png".format(f)
        img= pg.image.load(nome_arquivo).convert_alpha()
        img= pg.transform.scale(img,(WIDTH_P,HEIGHT_P))
        PF_Anim.append(img)
    assets["player_walk"] = PF_Anim
    #Pulando
    PJ_Anim = []
    for j in range (0,6):
        nome_arquivo = "Jogador/PlayerJumpUp/{}.png".format(j)
        img =pg.image.load(nome_arquivo).convert_alpha()
        img = pg.transform.scale(img,(WIDTH_P,HEIGHT_P))
        PJ_Anim.append(img)
    assets["player_jump"] = PJ_Anim
    #Atirando
    PS_Anim = []
    for s in range (0,8):
        nome_arquivo = "Jogador/PlayerShooting/{}.png".format(s)
        img= pg.image.load(nome_arquivo).convert_alpha()
        img= pg.transform.scale(img,(WIDTH_P,HEIGHT_P))
        PS_Anim.append(img)
    assets["player_shoot"] = PS_Anim
    #Morrendo
    PD_Anim = []
    for s in range (1,3):
        nome_arquivo = "Jogador/Player/Death{}.png".format(s)
        img= pg.image.load(nome_arquivo).convert_alpha()
        img= pg.transform.scale(img,(WIDTH_P,HEIGHT_P))
        PD_Anim.append(img)
    assets["player_death"] = PD_Anim
    return assets  #Code em Cima