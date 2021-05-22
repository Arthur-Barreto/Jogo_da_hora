# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame as pg

pg.init()

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
sniper_img = pg.image.load("Inimigos/Soldado_inimigo/Atirando Esquerda/2.png").convert_alpha()
sniper_img = pg.transform.scale(sniper_img,(SNIPER_WIDTH,SNIPER_HEIGHT))
# erro do tiro parcialmente consertado
# agora falta ajustar ele para sair da mesma altura da bala


# ----- Inicia estruturas de dados
# definindo a classe 
class Player(pg.sprite.Sprite):
    def __init__(self, img, all_sprites, all_balas, bala_img):
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

#SE TIVER ERRADO ISSO AQUI EM BAIXO É SO APAGA
class soldado(pg.sprite.Sprite):                             
    def __init__(self, img, all_sprites, all_balas_mob, bala_img,all_mobs):
         # construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 500
        self.rect.bottom = 280
        self.speedx = 0
        self.all_sprites = all_sprites
        self.all_balas_mob = all_balas_mob
        self.bala_img = bala_img
        self.all_mobs = all_mobs
    def update(self):
        self.rect.x += self.speedx
    def shoot_m(self):
        nova_balaa = Bala(self.bala_img,self.rect.bottom,self.rect.centerx)
        self.all_sprites.add(nova_balaa)
        self.all_balas_mob(nova_balaa)

class Shoot_m(pg.sprite.Sprite):
    def __init__(self,img,bottom,centerx):
        #Contrutor da classe mãe(Sprite)
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom - 10
        self.speedx = -5
    def update(self):
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
all_mobs = pg.sprite.Group()
# criando o jogador
player = Player(player_img, all_sprites, all_balas, bala_img)
all_sprites.add(player)
#Criando Mobs
mob = soldado(sniper_img, all_sprites, all_balas_mob, bala_img, all_mobs)
all_sprites.add(mob)
all_mobs.add(mob)

i=0
# ===== Loop principal =====
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
        #Verifica se Soltou alguma tecla
        if event.type == pg.KEYUP:
            if event.key == pg.K_d:
                player.speedx-=4
            if event.key == pg.K_a:
                player.speedx+=4
        if i%120:
            mob.shoot_m()
    # --------- Atualiza estado do jogo-------------
    # atualizando a posição do jogador
    all_sprites.update()

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


