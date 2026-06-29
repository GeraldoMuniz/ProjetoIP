import pygame
from personagens.personagem import Personagem
import math

class Boneco (Personagem):      #herda de personagem
    def __init__(self, nome = "Usuário", vida = 100, velocidade = 1, x = 400, y = 300, tamanho = 40): #valores padroes
        super().__init__(nome, vida, velocidade, x, y, tamanho)     #construtor já é chamado

    def movimento (self):    #especificidade (selecionar o boneco atual)
        teclas = pygame.key.get_pressed ()

        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.rect.x -= self.velocidade
        elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.rect.x += self.velocidade
        
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.rect.y -= self.velocidade
        elif teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.rect.y += self.velocidade


        self.limite_mapa ()    #verifica se ele mesmo nao ultrapassou o limite
