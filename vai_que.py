# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame as pg
import time

pg.init()
pg.mixer.init()

# ----- Gera tela principal
WIDTH = 1100
HEIGHT = 300
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Metal Slug da massa')


# ----- Inicia assets
#Dimensões Jogador
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 38
#Dimensões Sniper
SNIPER_WIDTH= 63
SNIPER_HEIGHT= 48
#Dimensões Vida
VIDA_WIDTH = 48
VIDA_HEIGHT = 44
#Dimensões Plataforma
PLATAFORMA_WIDTH = 200
PLATAFORMA_HEIGHT = 50
#Dimensões Bala
BALA_WIDTH = 12
BALA_HEIGHT = 10
#Defini tamanho da Tile
TILE_SIZE = 12.5
#Defini Aceleração gravitacional
GRAVITY = 1
#Defini Velocidade do Pulo
JUMP_SIZE = TILE_SIZE
#Defini a velocidade X
SPEED_X =5 
#Vidas
lifes = 2
#Defini Tipos de Tiles
PLATAFORMA = 0
BLOCK = 0
EMPTY = -1

#Mapas
MAP1 = [
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
    [BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK],
    [BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK,BLOCK]
]

font = pg.font.SysFont(None,48)
background = pg.image.load('Cenario/Montanha Clean 1100x300.png').convert()
#player_img = pg.image.load("Jogador/PlayerWalking/0.png").convert_alpha()
#player_img = pg.transform.scale(player_img, (PLAYER_WIDTH,PLAYER_HEIGHT))
bala_img = pg.image.load("Disparos_Direita/2.png").convert_alpha()
sniper_img = pg.image.load("Inimigos/Soldado_inimigo/Atirando Esquerda/0.png").convert_alpha()
sniper_img = pg.transform.scale(sniper_img,(SNIPER_WIDTH,SNIPER_HEIGHT))

# carrega os sons do jogo, agr sim papaizinho heheh
# por enquanto só esses mas jaja tem mais senhoras e senhores
pg.mixer.music.load("Sons/BGM2.wav")
pg.mixer.music.set_volume(0.1)
shoot_sound = pg.mixer.Sound("Sons/Shoot3.wav")
shoot_m_sound = pg.mixer.Sound("Sons/Shoot1.wav")
deeth_sound_m = pg.mixer.Sound("Sons/Death.wav")

#Definindo Assets
assets = {}

#=====Telas=====
#StartScreen
start_sc = []
start_sc.append(pg.image.load("Tela Inicial/TIS0.png").convert())
start_sc.append(pg.image.load("Tela Inicial/TIS1.png").convert())
assets["startsc_anim"] = start_sc
#Game Background
background=pg.image.load("Cenario/Montanha Clean 1100X300.png").convert()
assets["background"] = background
segunda_tela=pg.image.load("Cenario/waterfall0.png").convert()
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
    nome_arquivo = "Inimigos/Soldado_inimigo/Morrendo Direita/{}.png".format(me)
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

#Estados do personagem
STILL = 0
JUMPING = 1
FALLING = 2

# ----- Inicia estruturas de dados
# definindo a classe 
class Player(pg.sprite.Sprite):
    def __init__(self, assets, all_sprites, all_balas, bala_img,all_balar_player,row,column,blocks):
        # construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        #Carregando Assets de animações
        self.idle_anim = assets["player"]
        self.walk_anim = assets ["player_walk"]
        self.walke_anim = assets ["player_walke"]
        self.jump_anim = assets ["player_jump"]
        #Definindo imagem
        self.image = self.idle_anim[0]
        self.mask = pg.mask.from_surface(self.image)
        #Criando Retangulo
        self.rect = self.image.get_rect()
        #Definindo posicionamento
        self.rect.centerx = 40
        self.rect.centery = 250
        self.rect.bottom = 280
        #Definindo velocidades
        self.speedx = 0
        self.speedy = 0
        #Definindo Frame
        self.frame = 0
        #Chamando Groups necessarios
        self.all_sprites = all_sprites
        self.all_balas = all_balas 
        self.bala_img = bala_img
        self.all_balas_player = all_balas_player
        #Estado de animação - IDLE
        self.current_anim = "idle"
        self.state = STILL
        self.estado = "alive"
        #Velocidade/Tick de animação
        self.frame_ticks = 100
        #Atualizar Ticks
        self.last_update = pg.time.get_ticks()
        #Definindo blocks
        self.blocks = blocks
        #definindo colunas
        #self.rect.x =  column * TILE_SIZE
        #self.rect.bottom = row * TILE_SIZE

    def update(self):
        # atualiza a posição do nosso mostro
        #Andando em Y
        self.rect.y += self.speedy
        #Velocidade + gravidade
        self.speedy += GRAVITY
        #Atualiza estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        #Chegando colisões
        colisoes = pg.sprite.spritecollide (self,self.blocks,False)
        for colisao in colisoes:
            if self.speedy > 0:
                self.rect.bottom = colisao.rect.top
                #Parar de cair - se colidir
                self.speedy = 0
                #Altera state
                self.state = STILL
            elif self.speedy < 0:
                self.rect.top = colisao.rect.bottom
                #Se Colidiu = Para de cair
                self.speedy = 0
                #Altera state
                self.state = STILL
        #Andando em X
        self.rect.x += self.speedx
        #manter o nosso lek na tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH 
        if self.rect.left < 0:
            self.rect.left = 0
        #Checa colisões
        colisoes = pg.sprite.spritecollide(self,self.blocks,False)
        for colisao in colisoes:
            #Indo para a direita
            if self.speedx > 0:
                self.rect.right = colisao.rect.left
            #indo para esquerda
            elif self.speedx < 0:
                self.rect.left = colisao.rect.right
        #Checando estado
        if self.speedx == 0:
            self.idle()
        elif self.speedx > 0:
            self.walk()
        elif self.speedx < 0:
            self.walke()
        if self.speedy > 0:
            if self.state == STILL:
                self.speedy -=JUMP_SIZE
                self.state = JUMPING
                self.jump()


    def idle (self):
        if self.current_anim != "idle":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "idle"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.idle_anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.idle_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    def walk (self):
        if self.current_anim != "walk":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "walk"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.walk_anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.walk_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def walke (self):
        if self.current_anim != "walk":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "walk"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.walke_anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.walke_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def jump (self):
        if self.current_anim != "jump":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "jump"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.jump_anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.jump_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    def shoot(self):
        #Gera Bala para direita
        if self.estado == "alive":
            nova_bala = Bala(self.bala_img,self.rect.bottom,self.rect.centerx)
            self.all_sprites.add(nova_bala)
            self.all_balas.add(nova_bala)
            self.all_balas_player.add(nova_bala)
            shoot_sound.play()

    def death (self):
        self.estado = "death"
        self.kill()

class Tile (pg.sprite.Sprite):
    #Construtor da classe
    def __init__ (self,title_img,row,column):
        #Construtor da classe Sprite
        pg.sprite.Sprite.__init__(self)
        #Defini IMG
        img = tile_img
        #Transforma o Tamanho do Tile
        img = pg.transform.scale(img,(12,12))
        #Defini a imagem de Self
        self.image = img
        self.mask = pg.mask.from_surface(self.image)
        #Cria posicionamnto
        self.rect = self.image.get_rect()
        #Posiciona o tile
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row

class Bala(pg.sprite.Sprite):
    def __init__(self,img, bottom,centerx): 
        #Construtor da classe mãe (Sprite)
        # se vc é do próximo periodo e está lendo
        # esse bagui de sprite é coonfuso, olha e faz parecido
        # e percebe o que muda
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #self.rect.centerx = 45
        #self.rect.bottom = 260
        self.rect.centerx = centerx
        self.rect.bottom = bottom - 15
        # a nossa bala corre para a direita, dai tem que ter velocidade
        # no eixo x não no y igual o do ex da nave
        self.speedx = 5
        # como vai para a direita a velocidade é positiva
    
    def update(self):
        #Atualiza a posição da Bala
        # lembrando que a a bala só se move no eixo x
        self.rect.x += self.speedx
        #Se Bala sair da Tela = KILL
        if self.rect.right > WIDTH:
            self.kill()
        # verifica se houve colisão entre tiro e o soldado inimigo
        '''
        hits = pg.sprite.spritecollide(self,all_mobs,True)
        for hit in hits:
            deeth_sound_m.play()
            self.kill()
        '''
#SE TIVER ERRADO ISSO AQUI EM BAIXO É SO APAGA
class Soldado(pg.sprite.Sprite):                             
    def __init__(self,assets,blocks, img, all_sprites, all_balas_mob, bala_img,all_players,x,bottom):
         # construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        #Carregando assets de animação
        self.corre_esque = assets["inim_corrE"]
        self.atirE = assets["inim_atirE"]
        self.dispE = assets ["disparo_esquerda"]
        #Definind Imagem
        self.image = img
        self.rect = self.image.get_rect()
        #Definindo posicionamento
        self.rect.centerx = x
        self.rect.bottom = bottom
        #Definindo Velocidades
        self.speedx = -0.05
        #Definindo Frame
        self.frame = 0
        #Chamando Groups necessarios
        self.all_sprites = all_sprites
        self.all_balas_mob = all_balas_mob
        self.bala_img = bala_img
        self.all_players = all_players
        self.refe_pos_ini = x
        #Estado de animação - Idle
        self.current_anim = "idle"
        self.state = STILL
        self.estado = "alive"
        #Velocidade/Tick de animação
        self.frame_ticks = 100
        #Atualizar Ticks
        self.last_update = pg.time.get_ticks()
        self.last_shoot = pg.time.get_ticks()
        #Defindo blocks
        self.blocks = blocks

    def update(self):
        #Atualizando posição do Soldado
        #Andando em X
        self.rect.x += self.speedx
        # self.rect.x trata a posição no eixo x, com ele podemos fazer o soldado parar de andar
        if self.rect.x <= (self.refe_pos_ini - 80):
            self.speedx = 0
        #Checando estado
        if self.speedx < 0:
            self.walk()
        if self.speedx == 0:
            self.atirando()

    def walk(self):
        if self.current_anim != "walk":
            self.last_update = pg.time.get_ticks()
            self.frame = 0
        self.current_anim = "walk"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.corre_esque):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.corre_esque[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    
    def atirando(self):
        
        if self.current_anim != "atirando":
            self.last_update = pg.time.get_ticks()
            self.frame = 0
        self.current_anim = "atirando"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.atirE):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.atirE[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    
    def shoot_m(self):
        
        if self.current_anim != "walk":
            nova_bala = Shoot_m(self.bala_img,self.rect.bottom,self.rect.centerx)
            self.all_sprites.add(nova_bala)
            self.all_balas_mob.add(nova_bala)
            shoot_m_sound.play()
            self.last_shoot = pg.time.get_ticks()
    
class Shoot_m(pg.sprite.Sprite):
    def __init__(self,img,bottom,centerx):
        #Contrutor da classe mãe(Sprite)
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom - 20
        self.speedx = -5 # velocidade fixa para a esquerda
        

    def update(self):
        # a bala só se move no eixo x, no sentido negativo
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.kill()

class Coracoes(pg.sprite.Sprite):
    def __init__ (self, img, all_sprites):
        #Construtor da classe mãe(Sprite)
        pg.sprite.Sprite.__init__(self)
        stat_vida = assets["stat_vida"] 
        self.cheia = stat_vida[0]
        self.meia = stat_vida[1]
        self.pouca = stat_vida[2]
        self.image = self.cheia
        self.rect = self.image.get_rect()
        self.rect.centerx = 60
        self.rect.bottom = 75
        self.all_sprites = all_sprites
        self.current_anim = "cheio"
    
    def dois(self):
        self.current_anim = "meio"
        self.image = self.meia
    
    def um (self):
        self.current_anim = "um"
        self.image = self.pouca

class Plataforma(pg.sprite.Sprite):
    def __init__(self,img,all_sprites,centerx,bottom):
        #Construtor da classe mãe(Sprite)
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx #1000
        self.rect.bottom = bottom #201
        self.all_sprites = all_sprites

    def remover(self):
        self.kill()
        

class Game(pg.sprite.Sprite):
    def __init__ (self):
        #Construtor da classe mãe(Sprite)
        self.state = "fase 1"
game = True

#Ajuste de velocidade
clock = pg.time.Clock()
FPS = 60

# Criando Grupos de Sprites
all_sprites = pg.sprite.Group()
all_balas = pg.sprite.Group()
all_balas_mob = pg.sprite.Group()
all_balas_player = pg.sprite.Group()
all_mobs = pg.sprite.Group()
all_players = pg.sprite.Group()
blocks = pg.sprite.Group()
# criando o jogador
player = Player(assets, all_sprites, all_balas, bala_img,all_balas_player, 12, 2, blocks)
all_players.add(player)
all_sprites.add(player)
#Criando Mostrador de Corações
coracao =  Coracoes(assets["stat_vida"], all_sprites)
all_sprites.add(coracao)
#Criando Class Game
game = Game()
#Adicionar Plataformas
if game.state == "fase 1":
    lista_centerx = [965,800]
    lista_bottom = [213,238]
    for e in range(0,2):
        plataforma = Plataforma((assets["plataforma"]), all_sprites, lista_centerx[e], lista_bottom[e])
        all_sprites.add(plataforma)
if game.state != "fase 1":
    plataforma = Plataforma((assets["plataforma"]), all_sprites, lista_centerx[e], lista_bottom[e])
    plataforma.remover()


#Criando Tiles de acordo com mapa
for row in range(len(MAP1)):
    for column in range(len(MAP1[row])):
        tile_type = MAP1[row][column]
        if tile_type == BLOCK:
            tile = Tile(tile_img,row,column)
            all_sprites.add(tile)
            blocks.add(tile)
#Criando Mobs

# primeiro for para os monstros de cima
grupo1_sol = [[600,285],[800,285],[1000,285]]
# segundo para os lek de baixo, é nois papaizinho
grupo2_sol = [[965,188],[800,213]]
for i in range(0,3):
    mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo1_sol[i][0],grupo1_sol[i][1])
    all_sprites.add(mob)
    all_mobs.add(mob)
for i in range(0,2):
    mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo2_sol[i][0],grupo2_sol[i][1])
    all_sprites.add(mob)
    all_mobs.add(mob)
# ===== Loop principal =====
i=0
# então, faltava só copiar essa linha para funfar a música de fundo
pg.mixer.music.play(loops=-1)
last_update = pg.time.get_ticks()
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pg.event.get():
        # ----- Verifica consequências
        if event.type == pg.QUIT:
            game = False
        # Verifica se apertou alguma tecla
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                player.speedx+=2
            if event.key == pg.K_a:
                player.speedx-=2
            if event.key == pg.K_w:
                if player.speedy <= 1:
                    player.speedy -= 15
            if event.key == pg.K_SPACE:
                player.shoot()

        #Verifica se Soltou alguma tecla
        if event.type == pg.KEYUP:
            if event.key == pg.K_d:
                player.speedx-=2
            if event.key == pg.K_a:
                player.speedx+=2
            if event.key == pg.K_w:
                player.speedy+=5
    for s in all_mobs:
        now = pg.time.get_ticks()
        
        if now - s.last_shoot > 1000 and s.rect.x - player.rect.x > 0 and s.rect.x - player.rect.x < 200:
            s.shoot_m()
            last_update = pg.time.get_ticks()
    # --------- Atualiza estado do jogo-------------
    # atualizando a posição do jogador
    all_sprites.update()

    # verifica se houve colisão entre tiro e o soldado inimigo

    hits = pg.sprite.groupcollide(all_mobs,all_balas_player,True,True, pg.sprite.collide_mask)

    hits = pg.sprite.spritecollide(player,all_balas_mob,True, pg.sprite.collide_mask)
    if len(hits) > 0:
        deeth_sound_m.play()
        for bala in all_balas_mob:
            bala.kill()
        if lifes <=0:
            player.death()
        lifes -= 1
    
    if lifes == 1:
        coracao.dois()
    if lifes == 0:
        coracao.um()
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0,0))

    # desenhando tudo que ta salvo em sprite
    all_sprites.draw(window)


    # ----- Atualiza estado do jogo
    pg.display.update()  # Mostra o novo frame para o jogador
    i+=1
# ===== Finalização =====
pg.quit()  # Função do PyGame que finaliza os recursos utilizados