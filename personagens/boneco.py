import pygame
from personagens.personagem import Personagem

class Boneco (Personagem):      #herda de personagem
    def __init__(self, nome = "Usuário", vida = 100, velocidade = 1, x = 795, y = 780, tamanho = 40): #valores padroes
        super().__init__(nome, vida, velocidade, x, y, tamanho)     #construtor já é chamado

    def movimento (self, paredes):    #especificidade (selecionar o boneco atual)
        teclas = pygame.key.get_pressed()
    
        #movimento horizontal
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.rect.x -= self.velocidade
    
            for parede in paredes:
                if self.rect.colliderect(parede):
                    self.rect.left = parede.right
    
        elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.rect.x += self.velocidade
    
            for parede in paredes:
                if self.rect.colliderect(parede):
                    self.rect.right = parede.left
    
        #movimento vertical
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.rect.y -= self.velocidade
    
            for parede in paredes:
                if self.rect.colliderect(parede):
                    self.rect.top = parede.bottom
    
        elif teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.rect.y += self.velocidade
    
            for parede in paredes:
                if self.rect.colliderect(parede):
                    self.rect.bottom = parede.top
    
        self.limite_mapa()    #verifica se ele mesmo nao ultrapassou o limite
