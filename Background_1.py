import pygame as pg
from Config import *
from Assets import *
from sprites import *

def game_screen(window):
    # variável para o ajuste de velocidade
    clock = pg.time.Clock()
    #carregando assets
    score = 0
    # então, faltava só copiar essa linha para funfar a música de fundo
    pg.mixer.music.play(loops=-1)
    last_update = pg.time.get_ticks()
    window = pg.display.set_mode((WIDTH, HEIGHT))
    fase1 = True
    while fase1:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pg.event.get():
            # ----- Verifica consequências
            if event.type == pg.QUIT:
                fase1 = False
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
                    score +=5

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
        
            if now - s.last_shoot > 2000 and s.rect.x - player.rect.x > 0 and s.rect.x - player.rect.x < 400 and player.estado != "death":
                s.shoot_m()
                last_update = pg.time.get_ticks()
        # --------- Atualiza estado do jogo-------------
        # atualizando a posição do jogador
        all_sprites.update()

        # verifica se houve colisão entre tiro e o soldado inimigo

        hits = pg.sprite.groupcollide(all_mobs,all_balas_player,True,True, pg.sprite.collide_mask)
        if len(hits) > 0:
            score += 1

        hits = pg.sprite.spritecollide(player,all_balas_mob,True, pg.sprite.collide_mask)
        if len(hits) > 0:
            deeth_sound_m.play()
            for bala in all_balas_mob:
                bala.kill()
            lifes -= 1
    
        if lifes == 1:
            coracao.dois()
        if lifes == 0:
            coracao.um()
        if lifes <0:
                player.death()
        if player.estado == "death":
            for bala in all_balas_mob:
                bala.kill()
            morte = True
        if len(all_players) == 0:
            fase1 = False
        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets["background"], (0,0))
        #  desenhando tudo que ta salvo em sprite
        all_sprites.draw(window)
        # ----- Atualiza estado do jogo
        pg.display.update()  # Mostra o novo frame para o jogador
        if score >= 5 and player.rect.x >= 1050:
            fase2 = False
            player.death()
            player.kill()
            all_sprites.empty()
            all_balas.empty()
            all_balas_mob.empty()
            all_balas_player.empty()
            all_mobs.empty()
            all_players.empty()
            blocks.empty()
