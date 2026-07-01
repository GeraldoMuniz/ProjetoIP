import pygame

class Personagem (pygame.sprite.Sprite):                            #herda classe existente para facilitar
    def __init__(self, nome, vida, velocidade, x, y, tamanho, cooldown_ataque = 1500):
        super().__init__()                      #recursos sprite
        self.nome = nome                        #construtor
        self.vida = vida
        self.velocidade = velocidade
        self.rect = pygame.Rect (x, y, tamanho, tamanho) #saber tudo sobre o personagem
        self.tamanho = tamanho
        self.cooldown_ataque = cooldown_ataque
        self.ultimo_ataque = 0

    def limite_mapa (self, largura_mapa = 1672, altura_mapa = 941):
        if (self.rect.x < 0):
            self.rect.x = 0                                    #nao deixa ultrapassar os limites da tela
        elif (self.rect.x > largura_mapa - self.tamanho):
            self.rect.x = largura_mapa - self.tamanho

        if (self.rect.y < 0):
            self.rect.y = 0
        elif (self.rect.y > altura_mapa - self.tamanho):
            self.rect.y = altura_mapa - self.tamanho


    def dano (self, quantidade):
        tempo = pygame.time.get_ticks ()
        if (tempo - self.ultimo_ataque >= self.cooldown_ataque):
            self.vida -= quantidade
            self.ultimo_ataque = tempo
                    #em desenvolvimento

