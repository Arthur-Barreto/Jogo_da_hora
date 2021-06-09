import pygame as pg
from Config import *
from Assets import *
import time

# ----- Inicia estruturas de dados
# definindo a classe 
class Player(pg.sprite.Sprite):
    def __init__(self, assets, all_sprites, all_balas, bala_img,all_balas_player,row,column,blocks,sound):
        # construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        #Carregando Assets de animações
        #essa linha carrega o som na classe
        self.shoot_sound = sound
        self.idle_anim = assets["player"]
        self.walk_anim = assets ["player_walk"]
        self.walke_anim = assets ["player_walke"]
        self.jump_anim = assets ["player_jump"]
        self.shoot_anim = assets ["player_shoot"]
        self.death_anim = assets["player_death"]
        #Definindo imagem
        self.image = self.idle_anim[0]
        self.mask = pg.mask.from_surface(self.image)
        #Criando Retangulo
        self.rect = self.image.get_rect()
        #Definindo posicionamento
        self.rect.centerx = 40
        self.rect.centery = 250
        self.rect.bottom = 280
        #Definindo velocidades
        self.speedx = 0
        self.speedy = 0
        #Definindo Frame
        self.frame = 0
        #Chamando Groups necessarios
        self.all_sprites = all_sprites
        self.all_balas = all_balas 
        self.bala_img = bala_img
        self.all_balas_player = all_balas_player
        #Estado de animação - IDLE
        self.current_anim = "idle"
        self.state = STILL
        self.estado = "alive"
        #Velocidade/Tick de animação
        self.frame_ticks = 100
        #Atualizar Ticks
        self.last_update = pg.time.get_ticks()
        self.last_shoot = pg.time.get_ticks()
        #Definindo blocks
        self.blocks = blocks
        #definindo colunas
        #self.rect.x =  column * TILE_SIZE
        #self.rect.bottom = row * TILE_SIZE

    def update(self):
        if self.estado != "death":
            # atualiza a posição do nosso mostro
            #Andando em Y
            self.rect.y += self.speedy
            #Velocidade + gravidade
            self.speedy += GRAVITY
            #Atualiza estado para caindo
            if self.speedy > 0:
                self.state = FALLING
            #Chegando colisões
            colisoes = pg.sprite.spritecollide(self,self.blocks,False)
            for colisao in colisoes:
                if self.speedy > 0:
                    self.rect.bottom = colisao.rect.top
                    #Parar de cair - se colidir
                    self.speedy = 0
                    #Altera state
                    self.state = STILL
                elif self.speedy < 0:
                    self.rect.top = colisao.rect.bottom
                    #Se Colidiu = Para de cair
                    self.speedy = 0
                    #Altera state
                    self.state = STILL
            #Andando em X
            self.rect.x += self.speedx
            #manter o nosso lek na tela
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH 
            if self.rect.left < 0:
                self.rect.left = 0
            #Checa colisões
            colisoes = pg.sprite.spritecollide(self,self.blocks,False)
            for colisao in colisoes:
                #Indo para a direita
                if self.speedx > 0:
                    self.rect.right = colisao.rect.left
                #indo para esquerda
                elif self.speedx < 0:
                    self.rect.left = colisao.rect.right
            #Checando estado
            if self.speedx == 0:
                self.idle()
            elif self.speedx > 0:
                self.walk()
            elif self.speedx < 0:
                self.walke()
            if self.speedy > 0:
                if self.state == STILL:
                    self.speedy -=JUMP_SIZE
                    self.state = JUMPING
                    self.jump()
        if self.estado == "death":
            self.morrendo()
                
    def idle (self):
        if self.current_anim != "idle":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "idle"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.idle_anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.idle_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def walk (self):
        if self.current_anim != "walk":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "walk"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.walk_anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.walk_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def walke (self):
        if self.current_anim != "walke":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "walke"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.walke_anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.walke_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def jump (self):
        if self.current_anim != "jump":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "jump"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.jump_anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.jump_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def atirando_direita(self):
        if self.current_anim != "shoot_d":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "shoot_d"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.shoot_anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.shoot_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def shoot(self):
        #Gera Bala para direita
        if self.estado == "alive":
            if self.current_anim != "walke":
                self.atirando_direita()
                nova_bala = Bala(assets,self.bala_img,self.rect.bottom,self.rect.centerx)
                self.all_sprites.add(nova_bala)
                self.all_balas.add(nova_bala)
                self.all_balas_player.add(nova_bala)
                self.shoot_sound.play()
                self.last_shoot = pg.time.get_ticks()
            else:
                nova_bala = BalaE(assets,self.bala_img,self.rect.bottom,self.rect.centerx)
                self.all_sprites.add(nova_bala)
                self.all_balas.add(nova_bala)
                self.all_balas_player.add(nova_bala)
                self.shoot_sound.play()
                self.last_shoot = pg.time.get_ticks()
    
    def morrendo(self):
        if self.current_anim != "morrendo":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "morrendo"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.death_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.death_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def death (self):
        self.estado = "death"
        self.current_anim = "morrendo"
       


class Tile (pg.sprite.Sprite):
    #Construtor da classe
    def __init__ (self,title_img,row,column):
        #Construtor da classe Sprite
        pg.sprite.Sprite.__init__(self)
        #Defini IMG
        img = tile_img
        #Transforma o Tamanho do Tile
        img = pg.transform.scale(img,(12,12))
        #Defini a imagem de Self
        self.image = img
        self.mask = pg.mask.from_surface(self.image)
        #Cria posicionamnto
        self.rect = self.image.get_rect()
        #Posiciona o tile
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row

class Bala(pg.sprite.Sprite):
    def __init__(self,assets,img, bottom,centerx): 
        #Construtor da classe mãe (Sprite)
        # se vc é do próximo periodo e está lendo
        # esse bagui de sprite é coonfuso, olha e faz parecido
        # e percebe o que muda
        pg.sprite.Sprite.__init__(self)
        #Carregando Assets de animações
        self.shootd_anim = assets ["tiro_direta"]
        #Definindo Imagem
        self.image = img
        self.mask = pg.mask.from_surface(self.image)
        #Definindo retangulo
        self.rect = self.image.get_rect()
        #Definindo posicionamento
        #self.rect.centerx = 45
        #self.rect.bottom = 260
        self.rect.centerx = centerx
        self.rect.bottom = bottom - 15
        # a nossa bala corre para a direita, dai tem que ter velocidade
        # no eixo x não no y igual o do ex da nave
        #Definindo velocidade
        self.speedx = 5
        # como vai para a direita a velocidade é positiva
        #Definindo frame
        self.frame = 0
        #Estado de animação - Nulo
        self.current_anim = "nulo"
        #Velocidade/Tick de animação
        self.frame_ticks = 100
        #Atualizar ticks
        self.last_update = pg.time.get_ticks()

    
    def tiro_direita(self):
        if self.current_anim != "tiro_direita":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "tiro_direita"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.shootd_anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.shootd_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    
    def update(self):
        #Atualiza movimento bala
        self.rect.x += self.speedx
        #Se Bala sair da Tela = KILL
        if self.rect.right > WIDTH:
            self.kill()
        self.tiro_direita()
            
class BalaE(pg.sprite.Sprite):
    def __init__(self,assets,img, bottom,centerx): 
        #Construtor da classe mãe (Sprite)
        # se vc é do próximo periodo e está lendo
        # esse bagui de sprite é coonfuso, olha e faz parecido
        # e percebe o que muda
        pg.sprite.Sprite.__init__(self)
        #Carregando Assets de animações
        self.shoote_anim = assets ["tiro_esquerda"]
        #Definindo Imagem
        self.image = img
        self.mask = pg.mask.from_surface(self.image)
        #Definindo retangulo
        self.rect = self.image.get_rect()
        #Definindo posicionamento
        #self.rect.centerx = 45
        #self.rect.bottom = 260
        self.rect.centerx = centerx -5
        self.rect.bottom = bottom - 15
        # a nossa bala corre para a direita, dai tem que ter velocidade
        # no eixo x não no y igual o do ex da nave
        #Definindo velocidade
        self.speedx = -5
        # como vai para a direita a velocidade é positiva
        #Definindo frame
        self.frame = 0
        #Estado de animação - Nulo
        self.current_anim = "nulo"
        #Velocidade/Tick de animação
        self.frame_ticks = 100
        #Atualizar ticks
        self.last_update = pg.time.get_ticks()

    def tiro_esquerda(self):
        if self.current_anim != "tiro_esquerda":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "tiro_esquerda"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.shoote_anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.shoote_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    
    def update(self):
        #Atualiza movimento bala
        self.rect.x += self.speedx
        #Se Bala sair da Tela = KILL
        if self.rect.right > WIDTH:
            self.kill()
        self.tiro_esquerda()


#SE TIVER ERRADO ISSO AQUI EM BAIXO É SO APAGA
class Soldado(pg.sprite.Sprite):                             
    def __init__(self,assets,blocks, img, all_sprites, all_balas_mob, bala_img,all_players,x,ini,bottom,sound):
         # construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        #variavel para o som
        self.shoot_m_sound = sound
        #Carregando assets de animação
        self.corre_esque = assets["inim_corrE"]
        self.atirE = assets["inim_atirE"]
        self.dispE = assets ["disparo_esquerda"]
        self.death_anim = assets ["inim_morrE"]
        #Definind Imagem
        self.image = img
        self.rect = self.image.get_rect()
        #Definindo posicionamento
        self.rect.centerx = ini
        self.rect.bottom = bottom
        #Definindo Velocidades
        self.speedx = -0.05
        #Definindo Frame
        self.frame = 0
        #Chamando Groups necessarios
        self.all_sprites = all_sprites
        self.all_balas_mob = all_balas_mob
        self.bala_img = bala_img
        self.all_players = all_players
        self.refe_pos_ini = x
        #Estado de animação - Idle
        self.current_anim = "idle"
        self.state = STILL
        self.estado = "alive"
        #Velocidade/Tick de animação
        self.frame_ticks = 100
        #Atualizar Ticks
        self.last_update = pg.time.get_ticks()
        self.last_shoot = pg.time.get_ticks()
        #Defindo blocks
        self.blocks = blocks

    def update(self):
        if self.estado != "death":
            #Atualizando posição do Soldado
            #Andando em X
            self.rect.x += self.speedx
            # self.rect.x trata a posição no eixo x, com ele podemos fazer o soldado parar de andar
            if self.rect.x <= (self.refe_pos_ini - 80):
                self.speedx = 0
            #Checando estado
            if self.speedx < 0:
                self.walk()
            if self.speedx == 0:
                self.atirando()
        if self.estado == "death":
            self.morrendo()

    def walk(self):
        if self.current_anim != "walk":
            self.last_update = pg.time.get_ticks()
            self.frame = 0
        self.current_anim = "walk"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.corre_esque):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.corre_esque[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    
    def atirando(self):
        
        if self.current_anim != "atirando":
            self.last_update = pg.time.get_ticks()
            self.frame = 0
        self.current_anim = "atirando"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.atirE):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.atirE[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def shoot_m(self):
        if self.current_anim != "walk" and self.current_anim != "morrendo":
            nova_bala = Shoot_m(assets,self.bala_img,self.rect.bottom,self.rect.centerx)
            self.all_sprites.add(nova_bala)
            self.all_balas_mob.add(nova_bala)
            self.shoot_m_sound.play()
            self.last_shoot = pg.time.get_ticks()

    def morrendo(self):
        if self.current_anim != "morrendo":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "morrendo"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.death_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.death_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def death (self):
        self.estado = "death"
        self.current_anim = "morrendo"

class SoldadoD(pg.sprite.Sprite):                             
    def __init__(self,assets,blocks, img, all_sprites, all_balas_mob, bala_img,all_players,x,ini,bottom,sound):
         # construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        #variavel para o som
        self.shoot_m_sound = sound
        #Carregando assets de animação
        self.atirD = assets["inim_atirD"]
        self.dispD = assets ["tiro_direta"]
        self.death_anim = assets["inim_morrD"]
        #Definind Imagem
        self.image = img
        self.rect = self.image.get_rect()
        #Definindo posicionamento
        self.rect.centerx = ini
        self.rect.bottom = bottom
        #Definindo Velocidades
        self.speedx = 0
        #Definindo Frame
        self.frame = 0
        #Chamando Groups necessarios
        self.all_sprites = all_sprites
        self.all_balas_mob = all_balas_mob
        self.bala_img = bala_img
        self.all_players = all_players
        self.refe_pos_ini = x
        #Estado de animação - Idle
        self.current_anim = "idle"
        self.state = STILL
        self.estado = "alive"
        #Velocidade/Tick de animação
        self.frame_ticks = 100
        #Atualizar Ticks
        self.last_update = pg.time.get_ticks()
        self.last_shoot = pg.time.get_ticks()
        #Defindo blocks
        self.blocks = blocks

    def update(self):
        if self.estado != "death":
            #Atualizando posição do Soldado
            #Andando em X
            self.rect.x += self.speedx
            # self.rect.x trata a posição no eixo x, com ele podemos fazer o soldado parar de andar
            if self.rect.x <= (self.refe_pos_ini - 80):
                self.speedx = 0
            #Checando estado
            if self.speedx < 0:
                self.walk()
            if self.speedx == 0:
                self.atirando()
        if self.estado == "death":
            self.morrendo()
    
    def atirando(self):
        
        if self.current_anim != "atirando":
            self.last_update = pg.time.get_ticks()
            self.frame = 0
        self.current_anim = "atirando"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.atirD):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.atirD[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def morrendo(self):
        if self.current_anim != "morrendo":
            self.last_update = pg.time.get_ticks()
            self.frame = 0
        self.current_anim = "morrendo"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.death_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.death_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    
    def shoot_m(self):
        if self.current_anim != "walk" and self.current_anim != "morrendo":
            nova_bala = Shoot_mD(assets,self.bala_img,self.rect.bottom,self.rect.centerx)
            self.all_sprites.add(nova_bala)
            self.all_balas_mob.add(nova_bala)
            self.shoot_m_sound.play()
            self.last_shoot = pg.time.get_ticks()

    def death (self):
        self.estado = "death"
        self.current_anim = "morrendo"

class Kn(pg.sprite.Sprite):
    def __init__(self,assets,sound,centerx,bottom,all_balas_kn,all_sprites,bala_img):
        #Construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        #Variavel para o Som
        self.shoot_sound = sound
        #Carregando Assets de animação
        self.tiro_anim = assets["kt_atirando"]
        self.movimento_anim = assets["kt_movendo"]
        self.morrendo_anim = assets["kt_morrendo"]
        self.parado_anim = assets["kt_parado"]
        #Definindo Groups
        self.all_sprites = all_sprites
        self.all_balas_kn = all_balas_kn
        #Definindo Imagem
        self.image = img
        self.bala_img = bala_img
        self.rect = self.image.get_rect()
        #Definindo posicionamento
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        #Definindo velocidades
        self.speedx = 1
        #Definindo Frame
        self.frame = 0
        #Estado de animação - Idle
        self.current_anim = "idle"
        self.estado = "alive"
        #Velocidade/Tick de animação
        self.frame_ticks = 100
        #Atualizar Ticks
        self.last_update = pg.time.get_ticks()
        self.last_shoot = pg.time.get_ticks()
    
    def update(self):
        #Atualizando posição do Robo
        self.speedx += self.speedx
        if self.speedx == 0:
            self
    
    def atirando(self):
        if self.current_anim != "atirando":
            self.last_update = pg.time.get_ticks()
            self.frame = 0
        self.current_anim = "atirando"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.tiro_anim):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.tiro_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def morrendo(self):
        if self.current_anim != "morrendo":
            self.last_update = pg.time.get_ticks()
            self.frame = 0
        self.current_anim = "morrendo"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.morrendo_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.morrendo_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
    
    def shoot_m(self):
        if self.current_anim != "walk" and self.current_anim != "morrendo":
            nova_bala = Shoot_kn(assets,self.bala_img,self.rect.bottom,self.rect.centerx)
            self.all_sprites.add(nova_bala)
            self.all_balas_kn.add(nova_bala)
            self.shoot_m_sound.play()
            self.last_shoot = pg.time.get_ticks()

    def death (self):
        self.estado = "death"
        self.current_anim = "morrendo"


class Shoot_kn(pg.sprite.Sprite):
    def __init__(self,assets,img,bottom,centerx):
        #Construtor da classe mãe (Sprite)
        pg.sprite.Sprite.__init__(self)
        #Carregndo Assets de animação
        self.shoot = assets[""]
        #Definindo imagem
        self.image = img
        #Definindo Retangulo
        self.rect = self.image.get_rect()
        #Definindo Posicionamento
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        #Definindo velocidade
        self.speedx =-5
        #Definindo frame
        self.frame = 0
        #Estado de aniamção - NULO
        self.current_anim = "nulo"
        #Velocidade/Tick de animação
        self.frame_ticks = 100
        #Atualizar
        self.last_update = pg.time.get_ticks()
    
    def tiro(self):
        if self.current_anim != "tiro":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "tiro"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.shoot):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.shoot[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.kill()
        self.tiro()

class Shoot_m(pg.sprite.Sprite):
    def __init__(self,assets,img,bottom,centerx):
        #Contrutor da classe mãe(Sprite)
        pg.sprite.Sprite.__init__(self)
        #Carregando Assets de animação
        self.shoot = assets["disparo_esquerda"]
        #Definindo Imagem
        self.image = img
        #Defindo Retangulo
        self.rect = self.image.get_rect()
        #Definindo Posicionalmento
        self.rect.centerx = centerx
        self.rect.bottom = bottom - 20
        #Definod velocidades
        self.speedx = -5 # velocidade fixa para a esquerda
        #Definindo Frame
        self.frame = 0
        #Estado de animação - Nulo
        self.current_anim = "nulo"
        #Velocidade/Tick de animação
        self.frame_ticks = 100
        #Atualizar
        self.last_update = pg.time.get_ticks()

    def tiro(self):
        if self.current_anim != "tiro":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "tiro"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.shoot):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.shoot[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def update(self):
        # a bala só se move no eixo x, no sentido negativo
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.kill()
        self.tiro()

class Shoot_mD(pg.sprite.Sprite):
    def __init__(self,assets,img,bottom,centerx):
        #Contrutor da classe mãe(Sprite)
        pg.sprite.Sprite.__init__(self)
        #Carregando Assets de animação
        self.shoot = assets["tiro_direta"]
        #Definindo Imagem
        self.image = img
        #Defindo Retangulo
        self.rect = self.image.get_rect()
        #Definindo Posicionalmento
        self.rect.centerx = centerx
        self.rect.bottom = bottom - 20
        #Definod velocidades
        self.speedx = 5 # velocidade fixa para a esquerda
        #Definindo Frame
        self.frame = 0
        #Estado de animação - Nulo
        self.current_anim = "nulo"
        #Velocidade/Tick de animação
        self.frame_ticks = 100
        #Atualizar
        self.last_update = pg.time.get_ticks()

    def tiro(self):
        if self.current_anim != "tiro":
                self.last_update = pg.time.get_ticks()
                self.frame = 0
        self.current_anim = "tiro"
        now = pg.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            #Marca o tick da imagem
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.shoot):
                self.frame = 0
            else:
                center = self.rect.center
                self.image = self.shoot[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def update(self):
        # a bala só se move no eixo x, no sentido negativo
        self.rect.x += self.speedx
        if self.rect.right > 1100:
            self.kill()
        self.tiro()

class Coracoes(pg.sprite.Sprite):
    def __init__ (self, stat_vida, all_sprites):
        #Construtor da classe mãe(Sprite)
        pg.sprite.Sprite.__init__(self)
        self.cheia = stat_vida[0]
        self.meia = stat_vida[1]
        self.pouca = stat_vida[2]
        self.image = self.cheia
        self.rect = self.image.get_rect()
        self.rect.centerx = 60
        self.rect.bottom = 75
        self.all_sprites = all_sprites
        self.current_anim = "cheio"
    
    def dois(self):
        self.current_anim = "meio"
        self.image = self.meia
    
    def um (self):
        self.current_anim = "um"
        self.image = self.pouca

class Plataforma(pg.sprite.Sprite):
    def __init__(self,img,all_sprites,centerx,bottom):
        #Construtor da classe mãe(Sprite)
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx #1000
        self.rect.bottom = bottom #201
        self.all_sprites = all_sprites

    def remover(self):
        self.kill()
        

class Game(pg.sprite.Sprite):
    def __init__ (self):
        #Construtor da classe mãe(Sprite)
        self.state = "fase 1"
