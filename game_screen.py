import pygame as pg
from Config import *
from Assets import *
from sprites import *

def game_screen(window):
    # variável para o ajuste de velocidade
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

    DONE = 0
    PLAYING = 1
    DIEING = 2
    state = PLAYING

    keys_down = {}
    score = 0
    lifes = 2

    pg.mixer.music.play(loops=-1)
    last_update = pg.time.get_ticks()
    window = pg.display.set_mode((WIDTH, HEIGHT))
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

        # atualiza estado do jogo
        all_sprites.update()

        if state == PLAYING:
            # verifica se houve colisão entre tiro e o soldado inimigo

            hits = pg.sprite.groupcollide(all_mobs,all_balas_player,True,True, pg.sprite.collide_mask)
            for soldado in hits:
                ####### colocar a animação do soldado morrendo ########
                # ganhou pontos
                score += 1
            # essas duas partes veio do código antigo, precisamos testar de já
            # faz o score com essa parte de cima
            #if len(hits) > 0:
            #    score += 1

            #### agora verificamos colisao com o player
            hits = pg.sprite.spritecollide(player,all_balas_mob,True, pg.sprite.collide_mask)
            if len(hits) > 0:
                deeth_sound_m.play()
                player.kill()
                lifes -= 1
                ###### botar a animação dele morrendo #####
                state = DIEING
                keys_down = {}
                # tem que ajustar aqui de acordo com 
                morrendo_tick = pg.time.get_ticks()
                morrendo_duration = 
        elif state == DIEING:
            now = pg.time.get_ticks()
            if now - morrendo_tick > morrendo_duration:
                if lifes == 0:
                    state = DONE
                else:
                    state = PLAYING
                    player = 

            if lifes == 1:
                coracao.dois()
            if lifes == 0:
                coracao.um()
            if player.rect.x >=1050:
                score += 1
            # ----- Gera saídas
            window.fill((0, 0, 0))  # Preenche com a cor branca
            window.blit(assets["background"], (0,0))
            if score > 5:
                window.blit(assets["background2"],(0,0))
                player.death()
                game.state == "fase 2"


