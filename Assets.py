import pygame as pg
from Config import *
from Config import SC_HEIGHT,SC_HEIGHT,WIDTH,HEIGHT

# vamos carregar os assestes e os sons do jogo

font = pg.font.SysFont(None,48)
background = pg.image.load('Cenario/Montanha Clean 1100x300.png').convert()
bala_img = pg.image.load("Disparos_Direita/2.png").convert_alpha()
sniper_img = pg.image.load("Inimigos/Soldado_inimigo/Atirando Esquerda/0.png").convert_alpha()
sniper_img = pg.transform.scale(sniper_img,(SNIPER_WIDTH,SNIPER_HEIGHT))

# carrega os sons do jogo, agr sim papaizinho heheh
# por enquanto só esses mas jaja tem mais senhoras e senhores
pg.mixer.music.load("Sons/BGM2.wav")
pg.mixer.music.set_volume(0.05)
shoot_sound = pg.mixer.Sound("Sons/Shoot3.wav")
shoot_m_sound = pg.mixer.Sound("Sons/Shoot1.wav")
deeth_sound_m = pg.mixer.Sound("Sons/Death.wav")

#Definindo Assets
assets = {}


tile_img = pg.image.load("Imagem 50x50/0.png").convert_alpha()


#====Jogador====
    #Idle

PI_Anim = []
for e in range(0,11):
    nome_arquiva = "Jogador/PlayerIdle/{}.png".format(e)
    img = pg.image.load(nome_arquiva).convert_alpha()
    img = pg.transform.scale(img,(PLAYER_WIDTH,PLAYER_HEIGHT))
    PI_Anim.append(img)
assets["player"] = PI_Anim
#Andando Frente
PF_Anim = []
for f in range (0,15):
    nome_arquivo = "Jogador/PlayerWalking/Direita/{}.png".format(f)
    img= pg.image.load(nome_arquivo).convert_alpha()
    img= pg.transform.scale(img,(PLAYER_WIDTH,PLAYER_HEIGHT))
    PF_Anim.append(img)
assets["player_walk"] = PF_Anim

PFE_Anim = []
for f in range (0,15):
    nome_arquivo = "Jogador/PlayerWalking/Esquerda/{}.png".format(f)
    img= pg.image.load(nome_arquivo).convert_alpha()
    img= pg.transform.scale(img,(PLAYER_WIDTH,PLAYER_HEIGHT))
    PFE_Anim.append(img)
assets["player_walke"] = PFE_Anim
    #Pulando
PJ_Anim = []
for j in range (0,6):
    nome_arquivo = "Jogador/PlayerJumpUp/{}.png".format(j)
    img =pg.image.load(nome_arquivo).convert_alpha()
    img = pg.transform.scale(img,(PLAYER_WIDTH,PLAYER_HEIGHT))
    PJ_Anim.append(img)
assets["player_jump"] = PJ_Anim
    #Atirando
PS_Anim = []
for s in range (0,8):
    nome_arquivo = "Jogador/PlayerShooting/{}.png".format(s)
    img= pg.image.load(nome_arquivo).convert_alpha()
    img= pg.transform.scale(img,(PLAYER_WIDTH,PLAYER_HEIGHT))
    PS_Anim.append(img)
assets["player_shoot"] = PS_Anim
    #Morrendo
PD_Anim = []
for s in range (0,19):
    nome_arquivo = "Jogador/Player Dead/{}.png".format(s)
    img= pg.image.load(nome_arquivo).convert_alpha()
    img= pg.transform.scale(img,(PLAYER_WIDTH,PLAYER_HEIGHT))
    PD_Anim.append(img)
assets["player_death"] = PD_Anim

#====Inimigo===
    #Atirando Direita
ID = []
for idd in range (0,5):
    nome_arquivo = "Inimigos/Soldado_inimigo/Atirando Direita/{}.png".format(idd)
    img = pg.image.load(nome_arquivo).convert_alpha()
    img = pg.transform.scale(img,(SNIPER_WIDTH,SNIPER_HEIGHT))
    ID.append(img)
assets["inim_atirD"] = ID
    #Atirando Esquerda
IE = []
for ie in range (0,5):
    nome_arquivo = "Inimigos/Soldado_inimigo/Atirando Esquerda/{}.png".format(ie)
    img = pg.image.load(nome_arquivo).convert_alpha()
    img = pg.transform.scale(img,(SNIPER_WIDTH,SNIPER_HEIGHT))
    IE.append(img)
assets["inim_atirE"] = IE
    #Correndo Esquerda
CE = []
for ce in range (1,8):
    nome_arquivo = "Inimigos/Soldado_inimigo/Correndo Esquerda/{}.png".format(ce)
    img = pg.image.load(nome_arquivo).convert_alpha()
    img = pg.transform.scale(img,(SNIPER_WIDTH,SNIPER_HEIGHT))
    CE.append(img)
assets["inim_corrE"] = CE
    #Morrendo Direita
MD = []
for md in range (0,9):
    nome_arquivo = "Inimigos/Soldado_inimigo/Morrendo Direita/{}.png".format(md)
    img = pg.image.load(nome_arquivo).convert_alpha()
    img = pg.transform.scale(img,(SNIPER_WIDTH,SNIPER_HEIGHT))
    MD.append(img)
assets["inim_morrD"] = MD
    #Morrendo Esquerda
ME = []
for me in range (0,9):
    nome_arquivo = "Inimigos/Soldado_inimigo/Morrendo Esquerda/{}.png".format(me)
    img = pg.image.load(nome_arquivo).convert_alpha()
    img = pg.transform.scale(img,(SNIPER_WIDTH,SNIPER_HEIGHT))
    ME.append(img)
assets["inim_morrE"] = ME
    #Disparos a esquerda
DE = []
for de in range (1,10):
    nome_arquivo = "Disparos_Esquerda/{}.png".format(de)
    img = pg.image.load(nome_arquivo).convert_alpha()
    img = pg.transform.scale(img,(BALA_WIDTH,BALA_HEIGHT))
    DE.append(img)
assets["disparo_esquerda"] = DE

#====Vida====
vida = pg.image.load("Vida/Vida.png").convert_alpha()
vida = pg.transform.scale (vida,(VIDA_WIDTH,VIDA_HEIGHT))
meia_vida = pg.image.load("Vida/metade Vida.png").convert_alpha()
meia_vida = pg.transform.scale (meia_vida,(VIDA_WIDTH,VIDA_HEIGHT))
pouca_vida = pg.image.load("Vida/pouca Vida.png").convert_alpha()
pouca_vida = pg.transform.scale (pouca_vida,(VIDA_WIDTH,VIDA_HEIGHT))
vida_lista = [vida,meia_vida,pouca_vida]
assets["stat_vida"] = vida_lista

#====Plataformas====
plataforma = pg.image.load("plataformas/plataforma 1.png").convert_alpha()
plataforma = pg.transform.scale(plataforma,(PLATAFORMA_WIDTH,PLATAFORMA_HEIGHT))
assets["plataforma"] = plataforma
plataforma = pg.image.load("plataformas/plataforma 3.png").convert_alpha()
plataforma = pg.transform.scale(plataforma,(100,30))
assets["plataforma2"] = plataforma
#====Tiros====
    #Tiro para Direita
TD = []
for td in range(1,10):
    nome_arquivo = "Disparos_Direita/{}.png".format(td)
    img = pg.image.load(nome_arquivo).convert_alpha()
    img = pg.transform.scale(img,(BALA_WIDTH,BALA_HEIGHT))
    TD.append(img)
assets["tiro_direta"] = TD
    #Tiro para Esquerda
TE = []
for te in range(1,10):
    nome_arquivo = "Disparos_Esquerda/{}.png".format(te)
    img = pg.image.load(nome_arquivo).convert_alpha()
    img = pg.transform.scale(img,(BALA_WIDTH,BALA_HEIGHT))
    TE.append(img)
assets["tiro_esquerda"] = TE

#====Tela====   
    #Tela Inicial
start_sc = []
start_sc.append(pg.image.load("Tela Inicial/TIS0.png").convert())
start_sc.append(pg.image.load("Tela Inicial/TIS1.png").convert())
assets["startsc_anim"] = start_sc
    #Game Background
background=pg.image.load("Cenario/Montanha Clean 1100X300.png").convert()
assets["background"] = background
    #Game Background2
WT = []
for wt in range (0,8):
    nome_arquivo = "Cenario/waterfall{}.png".format(wt)
    img = pg.image.load(nome_arquivo).convert()
    img = pg.transform.scale (img,(WIDTH,HEIGHT))
    WT.append(img)
    WT.append(img)
assets["background2"] = WT
    #Tela Morte
TM = []
for tm in range(0,5):
    nome_arquivo = "GameOver/GM {}.png".format(tm*2)
    img = pg.image.load(nome_arquivo).convert()
    img = pg.transform.scale(img,(800,800))
    TM.append(img)
assets["tela_morte"] = TM
    #Loading
LO = []
for lo in range(0,12):
    nome_arquivo = "Tela de Carregamento/{}.png".format(lo)
    img = pg.image.load(nome_arquivo).convert()
    img = pg.transform.scale(img,(800,800))
    LO.append(img)
assets["loading"] = LO
    #Game Background 3
GB = []
for gb in range(0,40):
    nome_arquivo = "Cenario/boss{}.png".format(gb)
    img = pg.image.load(nome_arquivo).convert()
    img = pg.transform.scale(img,(WIDTH,HEIGHT))
    GB.append(img)
    GB.append(img)
    GB.append(img)
    GB.append(img)
assets["background3"] = GB
    #Tela Instruções
img = pg.image.load("Tela de Instrucoes/instru.png").convert()
img = pg.transform.scale(img,(800,800))
assets["info"] = img

#===== KT-21 =====
    #Parado
KTP = []
for ktp in range (0,2):
    nome_arquivo =  "Inimigos/kt-21/Parado/Parado-{}.png".format(ktp)
    img = pg.image.load(nome_arquivo).convert()
    img = pg.transform.scale(img,(KT_WIDTH,KT_HEIGHT))
    KTP.append(img)
assets["kt_parado"] = KTP
    #Atirando
KTA = []
for kta in range (0,18):
    nome_arquivo =  "Inimigos/kt-21/Atirando/Atirando-{}.png".format(kta)
    img = pg.image.load(nome_arquivo).convert()
    img = pg.transform.scale(img,(KT_WIDTH,KT_HEIGHT))
    KTA.append(img)
assets["kt_atirando"] = KTA
