#Importando Biblioteca Pygame
import pygame as pg
#Importando Arquivos e funções
from Config import *
from Assets import *
from sprites import *
from random import randint

#===== Fase 1
    #Função para Chamar Primeira Fase
def fase1(window,lifes):

    # estado do jogo é rodando
    jogo = RODANDO

    # chamando a fuunção clock
    clock = pg.time.Clock()

    # Criando Grupos de Sprites
    all_sprites = pg.sprite.Group()
    all_balas = pg.sprite.Group()
    all_balas_mob = pg.sprite.Group()
    all_balas_player = pg.sprite.Group()
    # balas do kn
    #all_balas_Kn = pg.sprite.Group()
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


    #Adicionando Plataformas
    #Criando Lista de Posições
    lista_centerx = [965,800]
    lista_bottom = [213,238]
    #For = Para criar diversas plataformas e Rodar listas
    for e in range(0,2):
        plataforma = Plataforma((assets["plataforma"]), all_sprites, lista_centerx[e], lista_bottom[e])
        all_sprites.add(plataforma)

    #Criando Tiles de acordo com mapa
    #For para as Linhas
    for row in range(len(MAP1)):
        #For para as Colunas
        for column in range(len(MAP1[row])):
            #Inicialização do Map1
            tile_type = MAP1[row][column]
            #Checagem de Tipo de Tile
            if tile_type == BLOCK:
                #Chama Sprite Tile = Criação de Tile
                tile = Tile(tile_img,row,column)
                #Adicionando Tile ao Group Sprites
                all_sprites.add(tile)
                #Adicionando Tile ao Group Blocks - Para realização de Colisões e adição de Física
                blocks.add(tile)
    
    #Criando Mobs
    #Definendo Lista dos Inimigos do Solo
    grupo1_sol = [[1100,285,600,-2],[1100,285,400,-1],[1100,285,200,-0.03]]
    #Definindo Lista dos Inimigos das plataformas
    grupo2_sol = [[965,188],[825,213]]
    #For para criar Mobs no Solo
    for i in range(0,3):
        mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo1_sol[i][0],WIDTH,grupo1_sol[i][1],shoot_sound,grupo1_sol[i][2],grupo1_sol[i][3])
        all_sprites.add(mob)
        all_mobs.add(mob)
    #For para criar Mobs nas plataformas
    for i in range(0,2):
        mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo2_sol[i][0],grupo2_sol[i][0],grupo2_sol[i][1],shoot_sound,0,0)
        all_sprites.add(mob)
        all_mobs.add(mob)

    #Definindo Score
    score = 0

    #Introduzindo Loop de Música
    pg.mixer.music.play(loops=-1)
    #Definindo Last_update
    last_update = pg.time.get_ticks()
    #Criando Janela com Width e Height Padronizados
    window = pg.display.set_mode((WIDTH, HEIGHT))
    #Definindo estado da fase 1
    fase1 = True
    #While Fase 1
    while fase1:
        #Definindo Tick Speed
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pg.event.get():
            # ----- Verifica consequências
            if event.type == pg.QUIT:
                fase1 = False
                state = QUIT
            # Verifica se apertou alguma tecla
            player.control(event,jogo)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    if jogo != PAUSADO:
                        pg.mixer.music.pause()
                        window.blit(pause_img, (150,0))
                        jogo = PAUSADO
                    else:
                        pg.mixer.music.unpause()
                        jogo = RODANDO
                if event.key == pg.K_x:
                    if jogo == PAUSADO:
                        fase1 = False
                        state = QUIT
                        break
                    

        if jogo == PAUSADO:
            pg.display.flip()
            continue


        #For para Chamar todos os inimigos dentro do Group Mobs
        for s in all_mobs:
            #Definindo Estado de Tick (No Agora)
            now = pg.time.get_ticks()
            #Criando If para definir se Mob ira atirar ou não, adicionando condições como posicionamento do Jogador, Quantos Ticks se passaram e estado do jogador
            if now - s.last_shoot > 2000 and s.rect.x - player.rect.x > 0 and s.rect.x - player.rect.x < 400 and player.estado != "death":
                #Chama Função de Tiro (Mob)
                s.shoot_m()
                #Atualiza Last_update
                last_update = pg.time.get_ticks()

        # --------- Atualiza estado do jogo-------------
        # atualizando a posição do jogador
        all_sprites.update()

        #Verifica se houve colisão entre tiro e o soldado inimigo
        hits = pg.sprite.groupcollide(all_mobs,all_balas_player,False,True, pg.sprite.collide_mask)
        #Se Houve colisões, o Jogador matou um Inimigo = Adiciona 1 Score
        for hit in hits:
            # mudar de estado o inimigo
            hit.death()
        if len(hits) > 0:
            score += 1

        #Verifica se houve colisões entre o Tiro dos Mobs e Player
        hits = pg.sprite.spritecollide(player,all_balas_mob,True, pg.sprite.collide_mask)
        #Se houve colisões, o Mob acertou o Jogador = Lifes - 1
        if len(hits) > 0:
            #Tocar Som de Dano
            deeth_sound_m.play()
            for bala in all_balas_mob:
                #Apagar todas as balas
                bala.kill()
            lifes -= 1

        #Se Lifes == 1 --> A animação de Coração será alterada
        if lifes == 1:
            coracao.dois()
        #Se Lifes == 2 --> A animação de Coração será alterada
        if lifes == 0:
            coracao.um()
        #Se Lifes < 1 --> Estado de jogador será alterado para Death, e o Estado Universal tambem.
        if lifes <0:
                player.death()
                state = DEATH
        #Se o Estado do Jogador for Death todas as balas que estão no AR serão deletadas
        if player.estado == "death":
            for bala in all_balas_mob:
                bala.kill()
            #Reforça que o Estado Universal  = Death
            state = DEATH
        #Quando a Animação for terminada o Jogador será deletado da pasta All_players. E isso tornará a fase1 Falsa.
        if len(all_players) == 0:
            fase1 = False
            #Reforça que o Estado Universal = Death
            state = DEATH
        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets["background"], (0,0))
        #  desenhando tudo que ta salvo em sprite
        all_sprites.draw(window)
        # ----- Atualiza estado do jogo
        pg.display.update()  # Mostra o novo frame para o jogador
        #Se o Jogador tiver Score 5 e atingir a posição 1050, ele passará de fase
        if score >= 5 and player.rect.x >= 1050:
            fase1 = False
            #Limpando todos os Groups
            player.death()
            player.kill()
            all_sprites.empty()
            all_balas.empty()
            all_balas_mob.empty()
            all_balas_player.empty()
            all_mobs.empty()
            all_players.empty()
            blocks.empty()
            #Definindo estado como LOAD
            state = LOAD
    return state

#===== Fase 2
    #Função para chamar Fase 2
def fase2(window,lifes):

    # definindo o estado do jogo como rodando

    jogo = RODANDO

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

    
    #Adicionar Plataformas
    #Criando Listas com posições
    lista_centerx = [650,675,540]
    lista_bottom = [228,137,145]
    #For para Criar plataformas
    for e in range(0,3):
        plataforma = Plataforma((assets["plataforma2"]), all_sprites, lista_centerx[e], lista_bottom[e])
        #Adicionando plataformas Sprite
        all_sprites.add(plataforma)

    #Criando Tiles de acordo com mapa
    #Definindo Row
    for row in range(len(MAP2)):
        #Definindo Coluna
        for column in range(len(MAP2[row])):
            #Carregando MAP2
            tile_type = MAP2[row][column]
            #Diferenciando Tile_type
            if tile_type == BLOCK:
                tile = Tile(tile_img,row,column)
                all_sprites.add(tile)
                blocks.add(tile)
    
    #Criando Mobs
    #Lista para Mobs do Solo
    grupo1_sol = [[1100,285,randint(200, 800),(randint(2,20)/10)],[1250,285,randint(350, 800),(randint(2,20)/10)],[1450,285,randint(500, 800),(randint(2,20)/10)]]
    grupo3_sol = [[1100,285,randint(200, 800),(randint(2,20)/10)],[1250,285,randint(350, 800),(randint(2,20)/10)],[1450,285,randint(500, 800),(randint(2,20)/10)],[1100,285,randint(200, 800),(randint(2,20)/10)],[1250,285,randint(350, 800),(randint(2,20)/10)],[1450,285,randint(500, 800),(randint(2,20)/10)],[1100,285,randint(200, 800),(randint(2,20)/10)],[1250,285,randint(350, 800),(randint(2,20)/10)],[1450,285,randint(500, 800),(randint(2,20)/10)],[1100,285,randint(200, 800),(randint(2,20)/10)],[1250,285,randint(350, 800),(randint(2,20)/10)],[1450,285,randint(500, 800),(randint(2,20)/10)]]
    #Lista para Mobs nas plataformas
    grupo2_sol = [[540,145,0,0],[550,145,0,0]]
    #For para criar Soldados no Chão
    for i in range(0,3):
        mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo1_sol[i][0],WIDTH,grupo1_sol[i][1],shoot_sound,grupo1_sol[i][2],-grupo1_sol[i][3])
        all_sprites.add(mob)
        all_mobs.add(mob)

    #Definindo Score
    score = 0

    #Acrescentando Loop Música
    pg.mixer.music.play(loops=-1)
    #Definindo last_Update
    last_update = pg.time.get_ticks()
    #Definindo tamanho de Window, com Width e Height padronizados
    window = pg.display.set_mode((WIDTH, HEIGHT))
    #Definindo estado Fase2
    fase2 = True
    #Definindo Variavel I
    i=0
    #While Fase2
    while fase2:
        #Definindo Clock
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pg.event.get():
            # ----- Verifica consequências
            if event.type == pg.QUIT:
                fase2 = False
                state = QUIT
            # Verifica se apertou alguma tecla
            player.control(event,jogo)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    if jogo != PAUSADO:
                        pg.mixer.music.pause()
                        window.blit(pause_img, (150,0))
                        jogo = PAUSADO
                    else:
                        pg.mixer.music.unpause()
                        jogo = RODANDO
                if event.key == pg.K_x:
                    if jogo == PAUSADO:
                        fase2 = False
                        state = QUIT
                        break
           
        if jogo == PAUSADO:
            pg.display.flip()
            continue

        #For para definir mobs dentro do Group Mobs
        for s in all_mobs:
            #Definindo Tick (No Agora)
            now = pg.time.get_ticks()
            #Adicionando variaveis para os Mobs atirarem, como Tempo, Posicionamento em X e estado do Player
            if now - s.last_shoot > 2000 and s.rect.x - player.rect.x > 0 and s.rect.x - player.rect.x < 400 and player.estado != "death":
                #Chama função dentro da Sprite Soldado
                s.shoot_m()
                #Atualiza last_update
                last_update = pg.time.get_ticks()
        # --------- Atualiza estado do jogo-------------
        # atualizando a posição do jogador
        all_sprites.update()

        #Verifica se houve colisão entre tiro e o soldado inimigo
        hits = pg.sprite.groupcollide(all_mobs,all_balas_player,False,True, pg.sprite.collide_mask)
        #Se Houve colisões, o Jogador matou um Inimigo = Adiciona 1 Score
        for hit in hits:
            # mudar de estado o inimigo
            hit.death()
        if len(hits) > 0:
            score += 1

        #Verifica se houve colisão entre Tiro dos solados e Player
        hits = pg.sprite.spritecollide(player,all_balas_mob,True, pg.sprite.collide_mask)
        if len(hits) > 0:
            #Play no Som de Dano
            deeth_sound_m.play()
            #Deleta todas as Balas
            for bala in all_balas_mob:
                bala.kill()
            #Retira uma Vida
            lifes -= 1

        #Se Lifes == 1 = Estado animação do Coração muda
        if lifes == 1:
            coracao.dois()
        #Se Lifes == 0 = Estado animação do Coração muda
        if lifes == 0:
            coracao.um()
        #Se Lifes < 0 = Definindo estado do Jogador
        if lifes <0:
                player.death()
                state = DEATH
        if player.estado == "death":
            for bala in all_balas_mob:
                bala.kill()
            #Reforça Estado de DEATH
            state = DEATH
        #Se Não existirem jogadores no Group All_Players
        if len(all_players) == 0:
            fase2 = False
            #Reforça Estado de Death
            state = DEATH
        if score >=3 and score <5 and len(all_mobs) <=1: 
            for i in range(0,3):
                mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo1_sol[i][0],WIDTH,grupo1_sol[i][1],shoot_sound,grupo1_sol[i][2],-grupo1_sol[i][3])
                all_sprites.add(mob)
                all_mobs.add(mob)
        if score >=6 and score <8 and len(all_mobs) <=1: 
            for i in range(0,6):
                mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo3_sol[i][0],WIDTH,grupo3_sol[i][1],shoot_sound,grupo3_sol[i][2],-grupo3_sol[i][3])
                all_sprites.add(mob)
                all_mobs.add(mob)
        if score >=9 and score <15 and len(all_mobs) <=1: 
            for i in range(0,3):
                mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo3_sol[i][0],WIDTH,grupo3_sol[i][1],shoot_sound,grupo3_sol[i][2],-grupo3_sol[i][3])
                all_sprites.add(mob)
                all_mobs.add(mob)
        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets["background2"][i%14], (0,0))
        #  desenhando tudo que ta salvo em sprite
        all_sprites.draw(window)
        # ----- Atualiza estado do jogo
        pg.display.update()  # Mostra o novo frame para o jogador
        #Se Score = 5 e Jogador está posicionado em pelo menos X = 1050 esté passa de nivel
        if score >= 5 and player.rect.x >= 1050:
            #Defini estado de Fase2 como False
            fase2 = False
            #Defini State como Carregando
            state = LOAD
            #Limpando Groups
            player.death()
            player.kill()
            all_sprites.empty()
            all_balas.empty()
            all_balas_mob.empty()
            all_balas_player.empty()
            all_mobs.empty()
            all_players.empty()
            blocks.empty()
        i+=1
    return state

def fase3(window,lifes):

    # defininfo o estado do jogo

    jogo = RODANDO

    #chamando a função clock
    clock = pg.time.Clock()

    # Criando Grupos de Sprites
    all_sprites = pg.sprite.Group()
    all_balas = pg.sprite.Group()
    all_balas_mob = pg.sprite.Group()
    all_balas_player = pg.sprite.Group()
    # # balas do kn
    all_balas_Kn = pg.sprite.Group()
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
    #Criando Barra de Vida Chefão
    barravida = Barravida(assets["barra_vida"], all_sprites)
    all_sprites.add(barravida)
    
  

    for row in range(len(MAP3)):
        #Definindo Coluna
        for column in range(len(MAP3[row])):
            #Carregando MAP2
            tile_type = MAP3[row][column]
            #Diferenciando Tile_type
            if tile_type == BLOCK:
                tile = Tile(tile_img,row,column)
                all_sprites.add(tile)
                blocks.add(tile)
    
    grupo3_sol = [[1100,285,randint(200, 800),(randint(2,20)/10)],[1250,285,randint(350, 800),(randint(2,20)/10)],[1450,285,randint(500, 800),(randint(2,20)/10)],[1125,285,randint(200, 800),(randint(2,20)/10)],[1275,285,randint(350, 800),(randint(2,20)/10)],[1475,285,randint(500, 800),(randint(2,20)/10)],[1150,285,randint(200, 800),(randint(2,20)/10)],[1300,285,randint(350, 800),(randint(2,20)/10)],[1500,285,randint(500, 800),(randint(2,20)/10)],[1175,285,randint(200, 800),(randint(2,20)/10)],[1325,285,randint(350, 800),(randint(2,20)/10)],[1525,285,randint(500, 800),(randint(2,20)/10)]]
    grupo1_sol = [[1100,285,randint(200, 800),(randint(2,20)/10)],[1250,285,randint(350, 800),(randint(2,20)/10)],[1450,285,randint(500, 800),(randint(2,20)/10)]]
    #For para criar Soldados no Chão
    for i in range(0,3):
        mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo1_sol[i][0],WIDTH,grupo1_sol[i][1],shoot_sound,grupo1_sol[i][2],-grupo1_sol[i][3])
        all_sprites.add(mob)
        all_mobs.add(mob)

    #Definindo Score
    score = 0
    Kn_lives = 15
    #Definindo estado Mobs
    mobs_state = "mobs"
    #Acrescentando Loop Música
    pg.mixer.music.play(loops=-1)
    #Definindo last_Update
    last_update = pg.time.get_ticks()
    #Definindo tamanho de Window, com Width e Height padronizados
    window = pg.display.set_mode((WIDTH, HEIGHT))
    #Definindo estado Fase2
    fase3 = True
    #Definindo Variavel I
    i=0
    #While Fase3
    while fase3:
        #Definindo Clock
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pg.event.get():
            # ----- Verifica consequências
            if event.type == pg.QUIT:
                fase3 = False
                state = QUIT
            player.control(event,jogo)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    if jogo != PAUSADO:
                        pg.mixer.music.pause()
                        window.blit(pause_img, (150,0))
                        jogo = PAUSADO
                    else:
                        pg.mixer.music.unpause()
                        jogo = RODANDO
                if event.key == pg.K_x:
                    if jogo == PAUSADO:
                        fase3 = False
                        state = QUIT
                        break

        if jogo == PAUSADO:
            pg.display.flip()
            continue

        ## chamando o boss fianl
        # boss final entra
        if len(all_mobs) <=0 and score >=18 and score <32:
            boss = Kn(assets,shoot_sound,WIDTH,280,all_balas_mob,all_sprites,bala_kn,WIDTH)
            all_sprites.add(boss)
            all_mobs.add(boss)
            mobs_state = "kn"
            
        
        #For para definir mobs dentro do Group Mobs
        if mobs_state == "mobs":
            for s in all_mobs:
                #Definindo Tick (No Agora)
                now = pg.time.get_ticks()
                #Adicionando variaveis para os Mobs atirarem, como Tempo, Posicionamento em X e estado do Player
                if now - s.last_shoot > 2000 and s.rect.x - player.rect.x > 0 and s.rect.x - player.rect.x < 600 and player.estado != "death":
                    #Chama função dentro da Sprite Soldado
                    s.shoot_m()
                    #Atualiza last_update
                    last_update = pg.time.get_ticks()
        if score >=3 and score <8 and len(all_mobs) <=1: 
            for i in range(0,6):
                mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo3_sol[i][0],WIDTH,grupo3_sol[i][1],shoot_sound,grupo3_sol[i][2],-grupo3_sol[i][3])
                all_sprites.add(mob)
                all_mobs.add(mob)
        if score >8 and score <16 and len(all_mobs) <=1: 
            for i in range(0,9):
                mob = Soldado(assets,blocks,sniper_img, all_sprites, all_balas_mob, bala_img, all_players,grupo3_sol[i][0],WIDTH,grupo3_sol[i][1],shoot_sound,grupo3_sol[i][2],-grupo3_sol[i][3])
                all_sprites.add(mob)
                all_mobs.add(mob)
        if mobs_state == "kn":
            for s in all_mobs:
                #Definindo Tick (No Agora)
                now = pg.time.get_ticks()
                #Adicionando variaveis para os Mobs atirarem, como Tempo, Posicionamento em X e estado do Player
                if now - s.last_shoot > 800 and player.estado != "death":
                    #Chama função dentro da Sprite Soldado
                    s.shoot_m()
                    #Atualiza last_update
                    last_update = pg.time.get_ticks()
        # --------- Atualiza estado do jogo-------------
        # atualizando a posição do jogador
        all_sprites.update()

        #Verifica se houve colisão entre tiro e o soldado inimigo
        if mobs_state == "mobs":
            hits = pg.sprite.groupcollide(all_mobs,all_balas_player,False,True, pg.sprite.collide_mask)
            #Se Houve colisões, o Jogador matou um Inimigo = Adiciona 1 Score
            for hit in hits:
                # mudar de estado o inimigo
                hit.death()
            if len(hits) > 0:
                score += 1
        if mobs_state == "kn":
            hits = pg.sprite.groupcollide(all_mobs,all_balas_player,False,True, pg.sprite.collide_mask)
            #Se Houve colisões, o Jogador matou um Inimigo = Adiciona 1 Score
            for hit in hits:
                # mudar de estado o inimigo
                Kn_lives-=1
                barravida.vidas()
                score += 1

        #Verifica se houve colisão entre Tiro dos solados e Player
        hits = pg.sprite.spritecollide(player,all_balas_mob,True, pg.sprite.collide_mask)
        if len(hits) > 0:
            #Play no Som de Dano
            deeth_sound_m.play()
            #Deleta todas as Balas
            for bala in all_balas_mob:
                bala.kill()
            #Retira uma Vida
            lifes -= 1

        #Se Lifes == 1 = Estado animação do Coração muda
        if lifes == 1:
            coracao.dois()
        #Se Lifes == 0 = Estado animação do Coração muda
        if lifes == 0:
            coracao.um()
        #Se Lifes < 0 = Definindo estado do Jogador
        if lifes <0:
                player.death()
                state = DEATH
        if player.estado == "death":
            for bala in all_balas_mob:
                bala.kill()
            #Reforça Estado de DEATH
            state = DEATH
        #Se Não existirem jogadores no Group All_Players
        if len(all_players) == 0:
            fase3 = False
            #Reforça Estado de Death
            state = DEATH
        # ----- Barra de Vida
        if Kn_lives <=0:
            boss.death()
        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(assets["background3"][i%160], (0,0))
        #  desenhando tudo que ta salvo em sprite
        all_sprites.draw(window)
        # ----- Atualiza estado do jogo
        pg.display.update()  # Mostra o novo frame para o jogador
        #Se Score = 3 e Jogador está posicionado em pelo menos X = 1050 esté passa de nivel
        if score >=20  and player.rect.x >= 1050 and len(all_mobs) ==  0:
            #Defini estado de Fase2 como False
            fase3 = False
            #Defini State como END, NOSSA FASE FINAL
            state = END
            #Limpando Groups
            player.death()
            player.kill()
            all_sprites.empty()
            all_balas.empty()
            all_balas_mob.empty()
            all_balas_player.empty()
            all_mobs.empty()
            all_players.empty()
            blocks.empty()
        i+=1
    return state

#===== Loading
    #Função para chamar Tela Loading
def loading(window):
    #Defini Clock
    clock = pg.time.Clock()
    #Adiciona Variavel I
    i=0
    #Defini FPS de Loading
    LOADING = 5
    #Defini estado da tela de Loading
    loading = True
    #Defini Dimensões da WIndow
    window = pg.display.set_mode((800, 800))
    #Inicia WHile
    while loading:
        #Defini Clock Speed
        clock.tick(LOADING)
        #Defini Plano de Fundo
        window.blit(assets["loading"][i%2],(0,0))
        #Verifica Eventos
        for event in pg.event.get():
            #Aperte Enter para começar / Quebrar Looping
            if event.type == pg.QUIT:
                loading = False
                state = QUIT
        #Atualiza Display
        pg.display.update()
        #Adiciona 1 a I
        i+=1
        #Se I for maior que 10, animação de Loading termina
        if i > 10:
            #Atualiza estado de Loading
            loading = False
            #Define estado Universal da proxima fase
            state = "FASE2"
    return state

def loading1(window):
    #Defini Clock
    clock = pg.time.Clock()
    #Adiciona Variavel I
    i=0
    #Defini FPS de Loading
    LOADING = 5
    #Defini estado da tela de Loading
    loading = True
    #Defini Dimensões da WIndow
    window = pg.display.set_mode((800, 800))
    #Inicia WHile
    while loading:
        #Defini Clock Speed
        clock.tick(LOADING)
        #Defini Plano de Fundo
        window.blit(assets["loading"][i%2],(0,0))
        #Verifica Eventos
        for event in pg.event.get():
            #Aperte Enter para começar / Quebrar Looping
            if event.type == pg.QUIT:
                loading = False
                state = QUIT
        #Atualiza Display
        pg.display.update()
        #Adiciona 1 a I
        i+=1
        #Se I for maior que 10, animação de Loading termina
        if i > 10:
            #Atualiza estado de Loading
            loading = False
            #Define estado Universal da proxima fase
            state = "FASE3"
    return state

#===== Tela da Morte
    #Função para chamar Tela da Morte
def death_screen(window):
    #Define Variavel de CLock
    clock = pg.time.Clock()
    #Define Variavel I
    i=0
    #Define FPS de LOADING
    LOADING = 1
    #Define Estado de Morte
    morte = True
    #Define Dimensões da Window
    window = pg.display.set_mode((800, 800))
    #Inicia While
    while morte:
        #Define a Clock Speed
        clock.tick(LOADING)
        #Define o Plano de fundo
        window.blit(assets["tela_morte"][i%5],(0,0))
        #Verifica eventos
        for event in pg.event.get():
            #Aperte Enter para começar / Quebrar Looping
            if event.type == pg.QUIT:
                loading = False
                state = QUIT
        pg.display.update()
        #Atualiza Variavel I
        i+=1
        #Se I maior que 5 (Diz que se passaram 5 Frames) = Atualiza estado de Morte + State Universal
        if i >= 5:
            morte = False
            state = INIT
    return state


#===== Tela da Vitoria
def final(window):
    #Define Variavel de CLock
    clock = pg.time.Clock()
    #Define Variavel I
    i=0
    #Define FPS de final
    FINAL = 2
    #Define Estado de final
    final = True
    #Define Dimensões da Window
    window = pg.display.set_mode((800, 800))
    #Inicia While
    while final:
        #Define a Clock Speed
        clock.tick(FINAL)
        #Define o Plano de fundo
        window.blit(assets["vitoria"][i%3],(0,0))
        #Verifica eventos
        for event in pg.event.get():
            #Aperte Enter para começar / Quebrar Looping
            if event.type == pg.QUIT:
                loading = False
                state = QUIT
        pg.display.update()
        #Atualiza Variavel I
        i+=1
        #Se I maior que 5 (Diz que se passaram 5 Frames) = Atualiza estado de Morte + State Universal
        if i >= 12:
            final = False
            state = INIT
    return state