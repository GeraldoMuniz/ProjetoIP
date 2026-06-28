import pygame

class Personagem (pygame.sprite.Sprite):                            #herda classe existente para facilitar
    def __init__(self, nome, vida, velocidade, x, y, tamanho):
        super().__init__()                      #recursos sprite
        self.nome = nome                        #construtor
        self.vida = vida
        self.velocidade = velocidade
        self.rect = pygame.Rect (x, y, tamanho, tamanho) #saber tudo sobre o personagem
        self.tamanho = tamanho

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
        self.vida -= quantidade
        if (self.vida <= 0):            #em desenvolvimento
            print ("perdeu")


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