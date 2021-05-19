from os import path

#Informações Gerais do jogo
FPS = 30
#Estabele a pasta que contem as figuras e sons
IMG_DIR = path.join(path.dirname(__file__),"assets","img")
#Cores básicas
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
#Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2