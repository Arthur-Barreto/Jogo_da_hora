import pygame as pg
from Config import *
from Assets import *
from sprites import *

def fase1(window,lifes):
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
    lista_centerx = [965,800]
    lista_bottom = [213,238]
    for e in range(0,2):
        plataforma = Plataforma((assets["plataforma"]), all_sprites, lista_centerx[e], lista_bottom[e])
        all_sprites.add(plataforma)

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

    #Definindo Score
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
                state = QUIT
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
                state = DEATH
        if player.estado == "death":
            for bala in all_balas_mob:
                bala.kill()
            state = DEATH
        if len(all_players) == 0:
            fase1 = False
            state = DEATH
        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets["background"], (0,0))
        #  desenhando tudo que ta salvo em sprite
        all_sprites.draw(window)
        # ----- Atualiza estado do jogo
        pg.display.update()  # Mostra o novo frame para o jogador
        if score >= 5 and player.rect.x >= 1050:
            fase1 = False
            player.death()
            player.kill()
            all_sprites.empty()
            all_balas.empty()
            all_balas_mob.empty()
            all_balas_player.empty()
            all_mobs.empty()
            all_players.empty()
            blocks.empty()
            state = LOAD
    return state

def fase2(window,lifes):
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

    #Criando Class Game
    game = Game()
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

    lista_centerx = [650,675,540]
    lista_bottom = [228,137,145]
    for e in range(0,3):
        plataforma = Plataforma((assets["plataforma2"]), all_sprites, lista_centerx[e], lista_bottom[e])
        all_sprites.add(plataforma)



    #Criando Tiles de acordo com mapa
    for row in range(len(MAP2)):
        for column in range(len(MAP2[row])):
            tile_type = MAP2[row][column]
            if tile_type == BLOCK:
                tile = Tile(tile_img,row,column)
                all_sprites.add(tile)
                blocks.add(tile)
    #Criando Mobs

    # primeiro for para os monstros de cima
    grupo1_sol = [[600,280],[800,280],[1000,280]]
    # segundo para os lek de baixo, é nois papaizinho
    grupo2_sol = [[540,145],[550,145]]
    for i in range(0,3):
        mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo1_sol[i][0],WIDTH,grupo1_sol[i][1],shoot_sound)
        all_sprites.add(mob)
        all_mobs.add(mob)
    for i in range(0,1):
        mob = SoldadoD(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo2_sol[i][0],grupo2_sol[i][0],grupo2_sol[i][1],shoot_sound)
        all_sprites.add(mob)
        all_mobs.add(mob)
    #carregando assets
    score = 0
    # então, faltava só copiar essa linha para funfar a música de fundo
    pg.mixer.music.play(loops=-1)
    last_update = pg.time.get_ticks()
    window = pg.display.set_mode((WIDTH, HEIGHT))
    fase2 = True
    while fase2:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pg.event.get():
            # ----- Verifica consequências
            if event.type == pg.QUIT:
                fase2 = False
                state = QUIT
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
                state = DEATH
        if player.estado == "death":
            for bala in all_balas_mob:
                bala.kill()
            state = DEATH
        if len(all_players) == 0:
            fase2 = False
            state = DEATH
        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets["background2"][0], (0,0))
        #  desenhando tudo que ta salvo em sprite
        all_sprites.draw(window)
        # ----- Atualiza estado do jogo
        pg.display.update()  # Mostra o novo frame para o jogador
        if score >= 5 and player.rect.x >= 1050:
            fase2 = False
            state = LOAD
            player.death()
            player.kill()
            all_sprites.empty()
            all_balas.empty()
            all_balas_mob.empty()
            all_balas_player.empty()
            all_mobs.empty()
            all_players.empty()
            blocks.empty()
    return state

def loading(window,indice):
    clock = pg.time.Clock()
    i=0
    LOADING = 5
    loading = True
    window = pg.display.set_mode((800, 800))
    while loading:
        clock.tick(LOADING)
        window.blit(assets["loading"][i%2],(0,0))
        for event in pg.event.get():
            #Aperte Enter para começar / Quebrar Looping
            if event.type == pg.QUIT:
                loading = False
                state = QUIT
        pg.display.update()
        i+=1
        if i > 10:
            loading = False
            state = ("FASE{}").format(indice)
    indice +=1
    return state

def death_screen(window):
    #Variavle para o ajuste de velocidade
    clock = pg.time.Clock()
    i=0
    LOADING = 1
    morte = True
    window = pg.display.set_mode((800, 800))
    while morte:
        clock.tick(LOADING)
        window.blit(assets["tela_morte"][i%5],(0,0))
        for event in pg.event.get():
            #Aperte Enter para começar / Quebrar Looping
            if event.type == pg.QUIT:
                loading = False
                state = QUIT
        pg.display.update()
        i+=1
        if i > 5:
            morte = False
            state = INIT
    return state