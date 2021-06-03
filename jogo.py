import pygame as pg
from Config import *
# iniciando o pyagme e o som do jogo
pg.init()
pg.mixer.init()
window = pg.display.set_mode((WIDTH, HEIGHT))

# importando todos os pacotes de configuração, som, imagem e clases
from Assets import *
from sprites import *

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


# gerando a tela principal

pg.display.set_caption('Metal Slug da massa')

# chamando a fuunção clock
clock = pg.time.Clock()

# Criando Grupos de Sprites
all_sprites = pg.sprite.Group()
all_balas = pg.sprite.Group()
all_balas_mob = pg.sprite.Group()
all_balas_player = pg.sprite.Group()
all_mobs = pg.sprite.Group()
all_players = pg.sprite.Group()
blocks = pg.sprite.Group()
# criando o jogador
player = Player(assets, all_sprites, all_balas, bala_img,all_balas_player, 12, 2, blocks,shoot_sound)
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
    mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo1_sol[i][0],WIDTH,grupo1_sol[i][1],shoot_sound)
    all_sprites.add(mob)
    all_mobs.add(mob)
for i in range(0,2):
    mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo2_sol[i][0],grupo2_sol[i][0],grupo2_sol[i][1],shoot_sound)
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
        
        if now - s.last_shoot > 2000 and s.rect.x - player.rect.x > 0 and s.rect.x - player.rect.x < 400:
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