import random
import pygame

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
