import pygame as pg
import os
Start_screen = "startsc_anim"

def load_assets():
    assets={}
    startsc_anim=[]
    for i in range (2):
        #Arquivos para animação - 0 a 1
        nome_arquivo = "Tela Inicial/TIS{}.png".format(i)
        img = pg.image.load(nome_arquivo).convert()
        img = pg.transform.scale (img,(0,0))
        startsc_anim.append(img)
    assets["startsc_anim"]=startsc_anim
    return assets


