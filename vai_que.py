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
font = pg.font.SysFont(None,48)
background = pg.image.load('Cenario/Montanha Clean 1100x300.png').convert()
player_img = pg.image.load("Jogador/PlayerWalking/0.png").convert_alpha()
player_img = pg.transform.scale(player_img, (PLAYER_WIDTH,PLAYER_HEIGHT))

BALA_WIDTH=4
BALA_HEIGHT=4
bala_img = pg.image.load("Disparos_Direita/2.png")
bala_img = pg.transform.scale(bala_img,(BALA_WIDTH,BALA_HEIGHT))

# ----- Inicia estruturas de dados
# definindo a classe 
class Player(pg.sprite.Sprite):
    def __init__(self, img, all_sprites, all_balas, bala_img):
        # construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.rect.bottom = 255
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
        nova_bala = Bala(self.bala_img,self.rect.centerx,self.rect.bottom)
        self.all_sprites.add(nova_bala)
        self.all_balas.add(nova_bala)

class Bala(pg.sprite.Sprite):
    def __init__(self,img): 
        #Construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = -10
    
    def update(self):
        #Atualiza a posição da Bala
        self.rect.x += self.speedx
        #Se Bala sair da Tela = KILL
        if self.rect.right > WIDTH:
            self.kill()
        if self.rect.left < 0:
            self.kill()

#SE TIVER ERRADO ISSO AQUI EM BAIXO É SO APAGA
class soldado(pg.sprite.Sprite):                             
    def __init__(self, img, all_sprites, all_balas, bala_img):
         # construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.rect.bottom = 255
        self.speedx = 0
        self.all_sprites = all_sprites
        self.all_balas = all_balas 
        self.bala_img = bala_img
#Classe pro soldado inimigo em cima



game = True
#Ajuste de velocidade
clock = pg.time.Clock()
FPS = 60

# criei aqui para dar bom
all_sprites = pg.sprite.Group()
all_balas = pg.sprite.Group()
# criando o jogador
bala = Bala(bala_img)
all_sprites.add(bala)
player = Player(player_img, all_sprites, all_balas, bala_img)
all_sprites.add(player)



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

# ===== Finalização =====
pg.quit()  # Função do PyGame que finaliza os recursos utilizados


