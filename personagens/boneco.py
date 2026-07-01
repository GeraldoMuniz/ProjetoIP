import pygame
from personagens.personagem import Personagem

class Boneco (Personagem):      #herda de personagem
    def __init__(self, nome = "Usuário", vida = 100, velocidade = 1, x = 795, y = 780, tamanho = 40): #valores padroes
        super().__init__(nome, vida, velocidade, x, y, tamanho)     #construtor já é chamado

        self.sprite_frente = pygame.image.load("imagem/vista_frente.png").convert_alpha()
        self.sprite_costas = pygame.image.load("imagem/vista_costas.png").convert_alpha()
        self.sprite_direita = pygame.image.load("imagem/vista_direita_dois.png").convert_alpha()
        self.sprite_esquerda = pygame.image.load("imagem/vista_esquerda.png").convert_alpha()

        #diminuir o tamanho
        self.sprite_frente = pygame.transform.scale(self.sprite_frente, (36, 52))
        self.sprite_costas = pygame.transform.scale(self.sprite_costas, (36, 52))
        self.sprite_direita = pygame.transform.scale(self.sprite_direita, (36, 52))
        self.sprite_esquerda = pygame.transform.scale(self.sprite_esquerda, (36, 52))

        #sprite inicial
        self.sprite = self.sprite_costas

    def movimento (self, paredes):    #especificidade (selecionar o boneco atual)
        teclas = pygame.key.get_pressed()
    
        #movimento horizontal
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.sprite = self.sprite_esquerda
            self.rect.x -= self.velocidade
    
            for parede in paredes:
                if self.rect.colliderect(parede):
                    self.rect.left = parede.right
    
        elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.sprite = self.sprite_direita
            self.rect.x += self.velocidade
    
            for parede in paredes:
                if self.rect.colliderect(parede):
                    self.rect.right = parede.left
    
        #movimento vertical
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.sprite = self.sprite_costas
            self.rect.y -= self.velocidade
    
            for parede in paredes:
                if self.rect.colliderect(parede):
                    self.rect.top = parede.bottom
    
        elif teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.sprite = self.sprite_frente
            self.rect.y += self.velocidade
    
            for parede in paredes:
                if self.rect.colliderect(parede):
                    self.rect.bottom = parede.top
    
        self.limite_mapa()    #verifica se ele mesmo nao ultrapassou o limite
