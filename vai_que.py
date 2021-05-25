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
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 38
SNIPER_WIDTH= 63
SNIPER_HEIGHT= 48
font = pg.font.SysFont(None,48)
background = pg.image.load('Cenario/Montanha Clean 1100x300.png').convert()
player_img = pg.image.load("Jogador/PlayerWalking/0.png").convert_alpha()
player_img = pg.transform.scale(player_img, (PLAYER_WIDTH,PLAYER_HEIGHT))
bala_img = pg.image.load("Disparos_Direita/2.png").convert_alpha()
sniper_img = pg.image.load("Inimigos/Soldado_inimigo/Atirando Esquerda/0.png").convert_alpha()
sniper_img = pg.transform.scale(sniper_img,(SNIPER_WIDTH,SNIPER_HEIGHT))

# carrega os sons do jogo, agr sim papaizinho heheh
# por enquanto só esses mas jaja tem mais senhoras e senhores
pg.mixer.music.load("Sons/BGM2.wav")
pg.mixer.music.set_volume(0.2)
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
for f in range (0,23):
    nome_arquivo = "Jogador/PlayerWalking/{}.png".format(f)
    img= pg.image.load(nome_arquivo).convert_alpha()
    img= pg.transform.scale(img,(PLAYER_WIDTH,PLAYER_HEIGHT))
    PF_Anim.append(img)
assets["player_walk"] = PF_Anim
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

# ----- Inicia estruturas de dados
# definindo a classe 
class Player(pg.sprite.Sprite):
    def __init__(self, img, all_sprites, all_balas, bala_img,all_balar_player):
        # construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 40
        self.rect.centery = 250
        self.rect.bottom = 280
        self.speedx = 0
        self.all_sprites = all_sprites
        self.all_balas = all_balas 
        self.bala_img = bala_img
        self.all_balas_player = all_balas_player
    
    def update(self):
        # atualiza a posição do nosso mostro
        self.rect.x += self.speedx

        #manter o nosso lek na tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH 
        if self.rect.left < 0:
            self.rect.left = 0
    
    def shoot(self):
        #Gera Bala
        nova_bala = Bala(self.bala_img,self.rect.bottom,self.rect.centerx)
        self.all_sprites.add(nova_bala)
        self.all_balas.add(nova_bala)
        self.all_balas_player.add(nova_bala)

class Bala(pg.sprite.Sprite):
    def __init__(self,img, bottom,centerx): 
        #Construtor da classe mãe (Sprite)
        # se vc é do próximo periodo e está lendo
        # esse bagui de sprite é coonfuso, olha e faz parecido
        # e percebe o que muda
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        #self.rect.centerx = 45
        #self.rect.bottom = 260
        self.rect.centerx = centerx
        self.rect.bottom = bottom -10
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
        hits = pg.sprite.spritecollide(self,all_mobs,True)
        for hit in hits:
            deeth_sound_m.play()
            mob.kill()
            self.kill()

#SE TIVER ERRADO ISSO AQUI EM BAIXO É SO APAGA
class Soldado(pg.sprite.Sprite):                             
    def __init__(self, img, all_sprites, all_balas_mob, bala_img,all_mobs):
         # construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 1100
        self.rect.bottom = 280
        self.speedx = -0.05
        self.all_sprites = all_sprites
        self.all_balas_mob = all_balas_mob
        self.bala_img = bala_img
        self.all_mobs = all_mobs
    def update(self):
        self.rect.x += self.speedx
        # self.rect.x trata a posição no eixo x, com ele podemos fazer o soldado parar de andar
        if self.rect.x <= 700:
            self.speedx = 0
    def shoot_m(self):
        nova_balaa = Shoot_m(self.bala_img,self.rect.bottom,self.rect.centerx)
        self.all_sprites.add(nova_balaa)
        self.all_balas_mob.add(nova_balaa)
    
class Shoot_m(pg.sprite.Sprite):
    def __init__(self,img,bottom,centerx):
        #Contrutor da classe mãe(Sprite)
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedx = -5 # velocidade fixa para a esquerda

    def update(self):
        # a bala só se move no eixo x, no sentido negativo
        self.rect.x += self.speedx
        if self.rect.left < WIDTH:
            self.kill()


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
# criando o jogador
player = Player(player_img, all_sprites, all_balas, bala_img,all_balas_player)
all_sprites.add(player)
#Criando Mobs
mob = Soldado(sniper_img, all_sprites, all_balas, bala_img, all_balas_mob)
all_sprites.add(mob)
all_mobs.add(mob)


# ===== Loop principal =====
i=0
# então, faltava só copiar essa linha para funfar a música de fundo
pg.mixer.music.play(loops=-1)
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
                player.speedx+=4
            if event.key == pg.K_a:
                player.speedx-=4
            if event.key == pg.K_SPACE:
                player.shoot()
            if event.key == pg.K_LSHIFT:
                mob.shoot_m()
        #Verifica se Soltou alguma tecla
        if event.type == pg.KEYUP:
            if event.key == pg.K_d:
                player.speedx-=4
            if event.key == pg.K_a:
                player.speedx+=4
    # --------- Atualiza estado do jogo-------------
    # atualizando a posição do jogador
    all_sprites.update()

    # verifica se houve colisão entre tiro e o soldado inimigo
    #hits = pg.sprite.spritecollide(mob,all_balas_player,True)
    
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