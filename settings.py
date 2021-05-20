import pygame as pg

class Settings():
    """ uma clase para armazenar todas as configurações do metal slug"""

    def __init__(self):
        """ inicializa as configurações do jogo """
        # configurações da tela do jogo
        self.screen_width = 1100
        self.screen_height = 300
        #configurações da tela do menu
        self.menu_width = 800
        self.menu_height = 800 
        # esse último é para a tela de fundo
        self.bg_color = (230,230,230)
    
class Player(pg.sprite.Sprite):
    """ clase relacionado para o jogador"""
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pg.sprite.Sprite.__init__(self)

        self.image = assets["player"]
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_width / 2
        self.rect.bottom = self.screen_height - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets

    def update(self):

        #atualiza a posição do jogador
        self.rect.x += self.speedx

        #mantem dentro da tela
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        new_bullet = Bullet(self.assets, self.rect.top, self.rect.centerx)
        self.groups['all_sprites'].add(new_bullet)
        self.groups['all_bullets'].add(new_bullet)
        #self.assets[PEW_SOUND].play()
    
    