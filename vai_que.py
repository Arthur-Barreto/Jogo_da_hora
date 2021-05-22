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
player_img = pg.image.load("Jogador/PlayerWalking/0.png")
player_img = pg.transform.scale(player_img, (PLAYER_WIDTH,PLAYER_HEIGHT))

# ----- Inicia estruturas de dados
# definindo a classe 
class Player(pg.sprite.Sprite):
    def __init__(self,img):
        # construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.rect.bottom = 250
        self.speedx = 0
    
    def update(self):
        # atualiza a posição do nosso mostro
        self.rect.x += self.speedx

        #manter o nosso lek na tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH 
        if self.rect.left < 0:
            self.rect.left = 0


game = True
#variável para ajuste de velocidade
clock = pg.time.Clock()
FPS = 60

# ele cria all sprites para os meteoros e usa o jogador nela
# criei aqui para dar bom
all_sprites = pg.sprite.Group()
# criando o jogador
player = Player(player_img)
all_sprites.add(player)

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pg.event.get():
        # ----- Verifica consequências
        if event.type == pg.QUIT:
            game = False
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


