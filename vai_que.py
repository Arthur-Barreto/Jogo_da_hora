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
player_img_walking = pg.image.load("Jogador/PlayerWalking/0.png")
player_img_walking_ajustado = pg.transform.scale(player_img_walking, (PLAYER_WIDTH,PLAYER_HEIGHT))

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pg.event.get():
        # ----- Verifica consequências
        if event.type == pg.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0,0))
    window.blit(player_img_walking_ajustado, (300, 200))

    # ----- Atualiza estado do jogo
    pg.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pg.quit()  # Função do PyGame que finaliza os recursos utilizados


