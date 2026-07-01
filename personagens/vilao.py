import pygame
from personagens.personagem import Personagem


class Inimigo (Personagem):
    def __init__(self, nome = "Inimigo", vida = 100, velocidade = 0.8, x = 100, y = 100, tamanho = 40, visao = 300):
        super().__init__(nome, vida, velocidade, x, y, tamanho)
        self.visao = visao
        self.posicao = pygame.math.Vector2 (x, y)     #declaração do campo de visao e posição do vilao

        self.sprite_frente = pygame.image.load("imagem/vilao_frente.png").convert_alpha()
        self.sprite_costas = pygame.image.load("imagem/vilao_costas.png").convert_alpha()
        self.sprite_direita = pygame.image.load("imagem/vilao_direita.png").convert_alpha()
        self.sprite_esquerda = pygame.image.load("imagem/vilao_esquerda.png").convert_alpha()

        self.sprite_frente = pygame.transform.scale(self.sprite_frente, (40, 56))
        self.sprite_costas = pygame.transform.scale(self.sprite_costas, (40, 56))
        self.sprite_direita = pygame.transform.scale(self.sprite_direita, (40, 56))
        self.sprite_esquerda = pygame.transform.scale(self.sprite_esquerda, (40, 56))

        self.sprite = self.sprite_frente

    def perseguir (self, alvo):
        posicao_alvo = pygame.math.Vector2 (alvo.rect.x, alvo.rect.y)

        vetor_direcao = posicao_alvo - self.posicao
        distancia = vetor_direcao.length()

        if (0 < distancia <= self.visao):
            direcao = vetor_direcao.normalize ()        #normalize deixa o vetor igual a 1, mas mantem apontando para o boneco

        if abs(direcao.x) > abs(direcao.y):
            if direcao.x > 0:
                self.sprite = self.sprite_direita
            else:
                self.sprite = self.sprite_esquerda
        else:
            if direcao.y > 0:
                self.sprite = self.sprite_frente
            else:
                self.sprite = self.sprite_costas

            self.posicao += direcao * self.velocidade       #o vetor que vale 1 é multiplicado pela velocidade a cada frame

            self.rect.x = int (self.posicao.x)
            self.rect.y = int (self.posicao.y)      #garantir que seja inteiro

            self.limite_mapa ()

    def verificar_colisao (self, alvo):             #verifica se encostou no boneco
        if (self.rect.colliderect (alvo.rect)):
            alvo.dano (1)
